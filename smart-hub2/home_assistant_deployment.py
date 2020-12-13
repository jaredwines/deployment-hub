from deployment import Deployment

class HomeAssistantDeployment(Deployment): 
   
    def deploy(self):
        return self.branch + self.host + self.gitRepo 
  