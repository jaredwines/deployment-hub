class Deployment:
    def __init__(self, git_repo, branch, project_dir, ssh_deployment_client):
        self._git_repo = git_repo
        self._project_dir = project_dir
        self._tmp_deploy_dir = project_dir + "/.tmp_deploy_process"
        self._branch = branch
        self._ssh_deployment_client = ssh_deployment_client

    @property
    def git_repo(self):
        return self._git_repo

    @git_repo.setter
    def git_repo(self, git_repo):
        self._git_repo = git_repo

    @property
    def tmp_deploy_dir(self):
        return self._tmp_deploy_dir

    @tmp_deploy_dir.setter
    def tmp_deploy_dir(self, tmp_deploy_dir):
        self._tmp_deploy_dir = tmp_deploy_dir

    @property
    def project_dir(self):
        return self._project_dir

    @project_dir.setter
    def project_dir(self, project_dir):
        self._project_dir = project_dir

    @property
    def branch(self):
        return self._branch

    @branch.setter
    def branch(self, branch):
        self._branch = branch


    @property
    def ssh_deployment_client(self):
        return self._ssh_deployment_client

    @branch.setter
    def ssh_deployment_client(self, ssh_deployment_client):
        self._bssh_deployment_client = ssh_deployment_client