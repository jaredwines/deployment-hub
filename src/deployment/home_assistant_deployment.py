from src.deployment.util.deployment_util import DeploymentUtil
from src.deployment.util.ssh_deployment_client import SshDeploymentClient
from src.model.deployment import Deployment


class HomeAssistantDeployment:

    def __init__(self, branch="master"):
        self.__deployment = Deployment("git@github.com:jaredwines/homeassistant-config.git", branch,
                                       "/home/jared/Projects/homeassistant-config")
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
    def backup_homeassistant(self):
        self.__ssh_deployment_client.exec_command(
            "git  -C " + self.__deployment.project_dir + " add --all")
        self.__ssh_deployment_client.exec_command(
            "git  -C " + self.__deployment.project_dir + " commit -m \"Backup.\"")
        self.__ssh_deployment_client.exec_command(
            "git  -C " + self.__deployment.project_dir + " push")

    def deploy(self):
        self._deployment_util.create_tmp_dir()
        self._deployment_util.clone_git_repo()
        self._deployment_util.move_deployment_contents()
        self._deployment_util.remove_tmp_dir()

        self.restart_docker()
