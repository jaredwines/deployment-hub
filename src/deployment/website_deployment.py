from src.deployment.util.deployment_website_util import DeploymentWebsiteUtil
from src.deployment.util.ssh_deployment_client import SshDeploymentClient
from src.model.deployment import Deployment


class WebsiteDeployment(DeploymentWebsiteUtil):

    def __init__(self, deployment):
        DeploymentWebsiteUtil.__init__(self, deployment)
        self._action = deployment.action

    def deploy_action(self):

        if self._action == "deploy":
            return self.deploy()

        elif self._action == "backup":
            return self.backup()

        # if self._action == "maintenance-mode":
        #     self.maintenance_flag = "True"
        #     return self.deploy()
