from deployment import Deployment

class HomeAssistantDeployment(Deployment): 

    def __init__(self, branch = "master"):
        super().__init__("smart-hub", "git@github.com:jaredwines/homeassistant-config.git", branch)
   
    def deploy(self):
        return self.branch + self.host + self.git_repo 
  