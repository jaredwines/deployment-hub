from src.deployment.util.deployment_website_util import DeploymentWebsiteUtil


class WebsiteDeployment(DeploymentWebsiteUtil):

    def __init__(self, deployment):
        DeploymentWebsiteUtil.__init__(self, deployment)
        self._action = deployment.action
        self._project_name = deployment.project_name
        self._deployment_type = deployment.deployment_type

    def deploy_action(self):

        if self._action == "deploy":
            return self.deploy()

        elif self._action == "backup":
            return self.backup()

        else:
            return ["Action: " + self._action + " not found for Project: " + self._project_name + " with Deployment Type: " + self._deployment_type + "!"]

        # if self._action == "maintenance-mode":
        #     self.maintenance_flag = "True"
        #     return self.deploy()
