from src.deployment.util.ssh_deployment_client import SshDeploymentClient
from src.model.deployment import Deployment

GIT_URL = "git@github.com:jaredwines/deployment-hub.git"
PROJECT_DIR = "/home/jared/Projects/deployment-hub"
SSH_HOSTNAME = "nuc"


class DeploymentHubDeployment:

    def __init__(self, branch="master"):
        self._deployment = Deployment(GIT_URL, branch, PROJECT_DIR, SshDeploymentClient(SSH_HOSTNAME))

    def update(self):
        self._deployment.ssh_deployment_client.exec_command(
            "sed -i '/DEPLOYMENT_HUB_BRANCH/c\DEPLOYMENT_HUB_BRANCH=" + self._deployment.branch + "' " +
            self._deployment.project_dir + "/.env")
        self._deployment.ssh_deployment_client.exec_command(
            "docker-compose --file " + self._deployment.project_dir + "/docker-compose.yml up --force-recreate --build -d")
