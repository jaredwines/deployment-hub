from local_deployment import LocalDeployment

class HomeAssistantDeployment(LocalDeployment): 

    def __init__(self):
        super().__init__("git@github.com:jaredwines/homeassistant-config.git", "/home/home-assistant")
   
    def deploy(self):
        return self.branch + self.host + self.git_repo 
  