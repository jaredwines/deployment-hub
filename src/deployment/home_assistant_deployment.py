from src.deployment.util.deployment_command import DeploymentCommand
from src.deployment.util.docker_command import DockerCommand
from src.deployment.util.ssh_deployment_client import SshDeploymentClient
from src.model.deployment import Deployment


class HomeAssistantDeployment(DockerCommand, DeploymentCommand):

    def __init__(self, branch="master"):
        self.__deployment = Deployment("git@github.com:jaredwines/homeassistant-config.git", branch,
                                       "/home/home-assistant")
        self.__ssh_deployment_client = SshDeploymentClient("smart-hub")

        self.__project_dir = self.__deployment.project_dir

        DockerCommand.__init__(self, self.__deployment, self.__ssh_deployment_client)
        DeploymentCommand.__init__(self, self.__deployment, self.__ssh_deployment_client)

    def start_docker(self):
        self.execute_docker_command(
            "docker-compose -f " + self.__project_dir + "/docker-compose.yml up -d")

    def restart_docker(self):
        self.execute_docker_command(
            "docker-compose -f " + self.__project_dir + "/docker-compose.yml restart")

    def stop_docker(self):
        self.execute_docker_command(
            "docker-compose -f " + self.__project_dir + "/docker-compose.yml stop")

    def update_docker(self):
        self.execute_docker_command(
            "docker-compose -f " + self.__project_dir + "/docker-compose.yml pull")
        self.execute_docker_command(
            "docker-compose -f " + self.__project_dir + "/docker-compose.yml up -d --build homeassistant")

    def deploy(self):
        self._create_tmp_dir()
        self._clone_git_repo()
        self._move_deployment_contents()
        self._remove_tmp_dir()

        self.restart_docker()
