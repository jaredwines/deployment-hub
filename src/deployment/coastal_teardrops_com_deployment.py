from src.deployment.util.deployment_website_util import DeploymentWebsiteUtil
from src.deployment.util.ssh_deployment_client import SshDeploymentClient
from src.model.deployment import Deployment

GIT_URL = "git@github.com:jaredwines/coastalteardrops.com.git"
PROJECT_DIR = "/home/dh_znrnx4/coastalteardrops.com"
SSH_HOSTNAME = "coastalteardrops"
DEPLOY_INCLUDE_LIST = None
DEPLOY_EXCLUDE_LIST = None


class CoastalTeardropsDeployment(DeploymentWebsiteUtil):

    def __init__(self, branch="master"):
        self._deployment = Deployment(GIT_URL, branch, PROJECT_DIR, SshDeploymentClient(SSH_HOSTNAME))
        DeploymentWebsiteUtil.__init__(self, self._deployment)
