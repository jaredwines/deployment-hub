from abc import ABC, abstractmethod 

class Deployment(ABC): 
    def __init__(self, host, gitRepo, branch):
        self._host = host
        self._gitRepo = gitRepo
        self._branch = branch
        super(Deployment, self).__init__()

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self,host):
        self._host=host

    @property
    def gitRepo(self):
        return self._gitRepo
    
    @gitRepo.setter
    def gitRepo(self,gitRepo):
        self._gitRepo=gitRepo

    @property
    def branch(self):
        return self._branch
    
    @branch.setter
    def branch(self,branch):
        self._branch=branch

    @abstractmethod
    def deploy(self):
        pass
  