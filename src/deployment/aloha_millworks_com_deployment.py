from src.deployment.util.deployment_website_util import DeploymentWebsiteUtil
from src.deployment.util.ssh_deployment_client import SshDeploymentClient
from src.model.deployment import Deployment

GIT_URL = "git@github.com:jaredwines/alohamillworks.com.git"
PROJECT_DIR = "/home/dh_guknsu/alohamillworks.com"
SSH_HOSTNAME = "alohamillworks"


class AlohaMillworksDeployment(DeploymentWebsiteUtil):

    def __init__(self, branch="master"):
        self._deployment = Deployment(GIT_URL, branch, PROJECT_DIR, SshDeploymentClient(SSH_HOSTNAME))
        DeploymentWebsiteUtil.__init__(self, self._deployment)


