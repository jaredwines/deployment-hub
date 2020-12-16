from abc import ABC, abstractmethod 

class Deployment(ABC): 
    def __init__(self, host, git_repo, project_dir):
        self._host = host
        self._git_repo = git_repo
        self._project_dir = project_dir
        self._tmp_deploy_dir = "~/.tmp_deploy_process"
        self._branch = "master"
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
    def tmp_deploy_dir(self):
        return self._tmp_deploy_dir
    
    @tmp_deploy_dir.setter
    def tmp_deploy_dir(self,tmp_deploy_dir):
        self._tmp_deploy_dir=tmp_deploy_dir

    @property
    def project_dir(self):
        return self._project_dir
    
    @project_dir.setter
    def project_dir(self,project_dir):
        self._project_dir=project_dir

    @property
    def branch(self):
        return self._branch
    
    @branch.setter
    def branch(self,branch):
        self._branch=branch

    @abstractmethod
    def make_dir(self, *target_dirs):
        pass

    @abstractmethod
    def clone_git_repo(self, target_dir = None):
        pass

    @abstractmethod
    def move_deployment_contents(self, source_dir = None, target_dir = None, regex = ".git*"):
        pass

    @abstractmethod
    def remove_dir(self, *target_dirs):
        pass

    @abstractmethod
    def create_tmp_dir(self):
        pass

    @abstractmethod
    def remove_tmp_dir(self):
        pass

    @abstractmethod
    def deploy(self):
        pass
  