from src.deployment.util.deployment_website_util import DeploymentWebsiteUtil
from src.deployment.util.ssh_deployment_client import SshDeploymentClient
from src.model.deployment import Deployment

GIT_URL = "git@github.com:jaredwines/jaredwines.com.git"
PROJECT_DIR = "/home/dh_agtzej/jaredwines.com"
SSH_HOSTNAME = "jaredwines"


class JaredWinesComDeployment(DeploymentWebsiteUtil):

    def __init__(self, branch="master"):
        self._deployment = Deployment(GIT_URL, branch, PROJECT_DIR, SshDeploymentClient(SSH_HOSTNAME))
        DeploymentWebsiteUtil.__init__(self, self._deployment)

    # def deploy(self):
    #     self._deployment_util.create_tmp_dir()
    #     self._deployment_util.clone_git_repo()
    #     self._deployment_util.move_deployment_contents()
    #     self._deployment_util.remove_tmp_dir()

    # self.configure_maintenance_mode()
