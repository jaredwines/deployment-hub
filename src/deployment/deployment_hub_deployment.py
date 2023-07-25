from src.deployment.util.deployment_file_util import DeploymentFileUtil
from src.deployment.util.ssh_deployment_client import SshDeploymentClient
from src.model.deployment import Deployment


class DeploymentHubDeployment:

    def __init__(self, branch="master"):
        self.__deployment = Deployment("git@github.com:jaredwines/homeassistant-config.git", branch,
                                       "/home/jared/Projects/deployment-hub")
        self.__ssh_deployment_client = SshDeploymentClient("nuc")
        self._deployment_util = DeploymentFileUtil(self.__deployment, self.__ssh_deployment_client)

    def update(self):
        self.__ssh_deployment_client.exec_command(
            "sed -i '/DEPLOYMENT_HUB_BRANCH/c\DEPLOYMENT_HUB_BRANCH=" + self.__deployment.branch + "' " +
            self.__deployment.project_dir + "/.env")
        self.__ssh_deployment_client.exec_command(
            "docker-compose --env-file " + self.__deployment.project_dir + "/.env --file " + self.__deployment.project_dir + "/docker-compose.yml up --force-recreate --build -d")
