from deployment import Deployment

class JaredWinesComDeployment(Deployment): 
   
    def deploy(self):    
       return self.branch + self.host + self.gitRepo 
  