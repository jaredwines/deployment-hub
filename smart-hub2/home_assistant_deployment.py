from deployment import Deployment

class HomeAssistantDeployment(Deployment): 

    def __init__(self, branch):
        self._host = "test"
        self._gitRepo = "test1"
        super().__init__(self._host, self._gitRepo, branch)
   
    def deploy(self):
        return self.branch + self.host + self.gitRepo 
  