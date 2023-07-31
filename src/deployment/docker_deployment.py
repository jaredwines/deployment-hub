from src.deployment.util.deployment_docker_util import DeploymentDockerUtil


class DockerDeployment(DeploymentDockerUtil):

    def __init__(self, deployment):
        DeploymentDockerUtil.__init__(self, deployment)
        self._action = deployment.action

    def deploy_action(self):

        if self._action == "deploy":
            return self.deploy()

        elif self._action == "start":
            return self.start_docker()

        elif self._action == "stop":
            return self.stop_docker()

        elif self._action == "restart":
            return self.restart_docker()

        elif self._action == "update":
            return self.update_docker()

        elif self._action == "backup":
            return self.backup()
