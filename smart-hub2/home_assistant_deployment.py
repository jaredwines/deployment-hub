from local_docker_deployment import LocalDockerDeployment

class HomeAssistantDeployment(LocalDockerDeployment): 

    def __init__(self):
        super().__init__("git@github.com:jaredwines/homeassistant-config.git", "/home/home-assistant")
   
    def deploy(self):
        super().deploy()
        self.restart()

  