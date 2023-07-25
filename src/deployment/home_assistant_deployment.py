from src.deployment.util.deployment_docker_util import DeploymentDockerUtil
from src.deployment.util.ssh_deployment_client import SshDeploymentClient
from src.model.deployment import Deployment

GIT_URL = "git@github.com:jaredwines/homeassistant-config.git"
PROJECT_DIR = "/home/jared/Projects/homeassistant-config"
SSH_HOSTNAME = "nuc"


class HomeAssistantDeployment(DeploymentDockerUtil):

    def __init__(self, branch="main"):
        self._deployment = Deployment(GIT_URL, branch, PROJECT_DIR, SshDeploymentClient(SSH_HOSTNAME))
        DeploymentDockerUtil.__init__(self, self._deployment)

    # def backup_homeassistant(self):
    #     self.__ssh_deployment_client.exec_command(
    #         "git -C " + self.__deployment.project_dir + " add --all")
    #     self.__ssh_deployment_client.exec_command(
    #         "git -C " + self.__deployment.project_dir + " commit -m \"Backup.\"")
    #     self.__ssh_deployment_client.exec_command(
    #         "git -C " + self.__deployment.project_dir + " push")
    #
    # def deploy(self):
    #     self._deployment_util.create_tmp_dir()
    #     self._deployment_util.clone_git_repo()
    #     self._deployment_util.move_deployment_contents()
    #     self._deployment_util.remove_tmp_dir()
    #
    #     self.restart_docker()
