from src.deployment.docker_deployment import DockerDeployment


class DeploymentManager:

    def __init__(self, deployment):
        self._deployment = deployment
        self._deployment_type = deployment.deployment_type

    def run(self):

        if self._deployment_type == "docker":
            docker_deployment = DockerDeployment(self._deployment)
            return docker_deployment.deploy_action()

        elif self._deployment_type == "website":
            return True

        else:
            return ["Deployment type not found!"]
