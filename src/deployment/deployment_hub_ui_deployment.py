from src.deployment.util.deployment_docker_util import DeploymentDockerUtil
from src.deployment.util.ssh_deployment_client import SshDeploymentClient
from src.model.deployment import Deployment

GIT_URL = "git@github.com:jaredwines/deployment-hub-ui.git"
PROJECT_DIR = "/home/jared/Projects/deployment-hub-ui"
SSH_HOSTNAME = "nuc"


class DeploymentHubUIDeployment:

    def __init__(self, branch="main"):
        self._deployment = Deployment(GIT_URL, branch, PROJECT_DIR, SshDeploymentClient(SSH_HOSTNAME))
        DeploymentDockerUtil.__init__(self, self._deployment)
