from deployment import Deployment

class JaredWinesComDeployment(Deployment): 

    def __init__(self, branch = "master", maintenance_flag = False):
        self._maintenance_flag = maintenance_flag
        self._host = "jaredwines.com"
        self._gitRepo = "git@github.com:jaredwines/jaredwines.com.git"
        super().__init__(self._host, self._gitRepo, branch)

    @property
    def maintenance_flag(self):
        return self._maintenance_flag

    @maintenance_flag.setter
    def maintenance_flag(self,maintenance_flag):
        self._maintenance_flag=maintenance_flag
   
    def deploy(self):    
       return self.branch + self.host + self.gitRepo + str(self.maintenance_flag)
  