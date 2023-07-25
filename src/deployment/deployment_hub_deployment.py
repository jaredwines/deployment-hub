from src.deployment.util.deployment_util import DeploymentUtil
from src.deployment.util.ssh_deployment_client import SshDeploymentClient
from src.model.deployment import Deployment


class DeploymentHubDeployment:

    def __init__(self, branch="master"):
        self.__deployment = Deployment("git@github.com:jaredwines/homeassistant-config.git", branch,
                                       "/home/jared/Projects/deployment-hub")
        self.__ssh_deployment_client = SshDeploymentClient("nuc")
        self._deployment_util = DeploymentUtil(self.__deployment, self.__ssh_deployment_client)

    def update(self):
        self.__ssh_deployment_client.exec_command(
            "docker-compose --file " + self.__deployment.project_dir + "/docker-compose.yml up --force-recreate --build -d")
