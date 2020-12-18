from deployment import Deployment

class HomeAssistantDeployment(Deployment): 

    def __init__(self):
        super().__init__("smart-hub", "git@github.com:jaredwines/homeassistant-config.git", "/home/home-assistant")
   
    def deploy(self):
        super().deploy()
        self.restart()

  