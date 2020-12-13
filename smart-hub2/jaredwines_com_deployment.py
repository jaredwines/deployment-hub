from deployment import Deployment

class JaredWinesComDeployment(Deployment): 

    def __init__(self, host, gitRepo, branch, maintenance_flag = False):
        self._maintenance_flag = maintenance_flag
        super().__init__(host, gitRepo, branch)

    @property
    def maintenance_flag(self):
        return self._maintenance_flag

    @maintenance_flag.setter
    def maintenance_flag(self,maintenance_flag):
        self._maintenance_flag=maintenance_flag
   
    def deploy(self):    
       return self.branch + self.host + self.gitRepo + self.maintenance_flag
  