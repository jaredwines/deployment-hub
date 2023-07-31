from src.deployment.docker_deployment import DockerDeployment
from src.deployment.website_deployment import WebsiteDeployment


class DeploymentManager:

    def __init__(self, deployment):
        self._deployment = deployment
        self._deployment_type = deployment.deployment_type
        self._project_name = deployment.project_name

    def run(self):

        if self._deployment_type == "docker":
            docker_deployment = DockerDeployment(self._deployment)
            return docker_deployment.deploy_action()

        elif self._deployment_type == "website":
            website_deployment = WebsiteDeployment(self._deployment)
            return website_deployment.deploy_action()

        else:
            return ["Deployment Type: " + self._deployment_type + " not found for Project: " + self._project_name + "!"]
