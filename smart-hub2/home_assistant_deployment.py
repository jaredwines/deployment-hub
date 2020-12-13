from deployment import Deployment

class HomeAssistantDeployment(Deployment): 

    def __init__(self, branch = "master"):
        self._host = "smart-hub"
        self._gitRepo = "git@github.com:jaredwines/homeassistant-config.git"
        super().__init__(self._host, self._gitRepo, branch)
   
    def deploy(self):
        return self.branch + self.host + self.gitRepo 
  