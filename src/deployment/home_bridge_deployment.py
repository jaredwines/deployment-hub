from src.deployment.util.deployment_util import DeploymentUtil
from src.deployment.util.ssh_deployment_client import SshDeploymentClient
from src.model.deployment import Deployment


class HomebridgeDeployment:

    def __init__(self, branch="main"):
        self.__deployment = Deployment("git@github.com:jaredwines/homebridge-config.git", branch,
                                       "/home/jared/Projects/homebridge-config")
        self.__ssh_deployment_client = SshDeploymentClient("nuc")
        self._deployment_util = DeploymentUtil(self.__deployment, self.__ssh_deployment_client)

    def start_docker(self):
        self.__ssh_deployment_client.exec_command(
            "docker-compose -f " + self.__deployment.project_dir + "/docker-compose.yml up -d")

    def restart_docker(self):
        self.__ssh_deployment_client.exec_command(
            "docker-compose -f " + self.__deployment.project_dir + "/docker-compose.yml restart")

    def stop_docker(self):
        self.__ssh_deployment_client.exec_command(
            "docker-compose -f " + self.__deployment.project_dir + "/docker-compose.yml stop")

    def update_docker(self):
        self.__ssh_deployment_client.exec_command(
            "docker-compose -f " + self.__deployment.project_dir + "/docker-compose.yml pull")
        self.__ssh_deployment_client.exec_command(
            "docker-compose -f " + self.__deployment.project_dir + "/docker-compose.yml up -d --build homeassistant")

    def backup_homebridge(self):
        command_list = []

        command_list.append("git -C " + self.__deployment.project_dir + " pull")
        command_list.append("git -C " + self.__deployment.project_dir + " add --all")
        command_list.append("git -C " + self.__deployment.project_dir + " commit -m \"Backup.\"")
        command_list.append("git -C " + self.__deployment.project_dir + " push")

        self.__ssh_deployment_client.exec_command(command_list)

    def deploy(self):
        self._deployment_util.create_tmp_dir()
        self._deployment_util.clone_git_repo()
        self._deployment_util.move_deployment_contents()
        self._deployment_util.remove_tmp_dir()

        self.restart_docker()
