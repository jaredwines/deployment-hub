from flask import current_app
from src.deployment.docker_deployment import DockerDeployment


class DeploymentManager:

    def __init__(self, deployment):
        self._deployment = deployment
        self._deployment_type = deployment.deployment_type

    def run(self):

        current_app.logger.info("run self")
        current_app.logger.info(self._deployment_type)
        if self._deployment_type == "docker":
            docker_deployment = DockerDeployment(self._deployment)
            current_app.logger.info("run self docker")
            return docker_deployment.deploy_action()

        elif self._deployment_type == "website":
            return True

        else:
            return ["Deployment type not found!"]