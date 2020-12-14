from abc import ABC, abstractmethod 

class Deployment(ABC): 
    def __init__(self, host, git_repo, branch):
        self._host = host
        self._git_repo = git_repo
        self._branch = branch
        super(Deployment, self).__init__()

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self,host):
        self._host=host

    @property
    def git_repo(self):
        return self._git_repo
    
    @git_repo.setter
    def git_repo(self,git_repo):
        self._git_repo=git_repo

    @property
    def branch(self):
        return self._branch
    
    @branch.setter
    def branch(self,branch):
        self._branch=branch

    @abstractmethod
    def deploy(self):
        pass
  