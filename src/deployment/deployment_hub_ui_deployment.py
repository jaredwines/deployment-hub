from src.deployment.util.deployment_docker_util import DeploymentDockerUtil
from src.deployment.util.ssh_deployment_client import SshDeploymentClient
from src.model.deployment import Deployment

GIT_URL = "git@github.com:jaredwines/deployment-hub-ui.git"
PROJECT_DIR = "/home/jared/Projects/deployment-hub-ui"
SSH_HOSTNAME = "nuc"


class DeploymentHubUIDeployment(DeploymentDockerUtil):

    def __init__(self, branch="main"):
        self._deployment = Deployment(GIT_URL, branch, PROJECT_DIR, SshDeploymentClient(SSH_HOSTNAME))
        DeploymentDockerUtil.__init__(self, self._deployment)

    def update(self):
        self._deployment.ssh_deployment_client.exec_command(
            "sed -i '/DEPLOYMENT_HUB_BRANCH/c\DEPLOYMENT_HUB_BRANCH=" + self._deployment.branch + "' " +
            self._deployment.project_dir + "/.env")
        self._deployment.ssh_deployment_client.exec_command(
            "docker-compose --file " + self._deployment.project_dir + "/docker-compose.yml up --force-recreate --build -d")
