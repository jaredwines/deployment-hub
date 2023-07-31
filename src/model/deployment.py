from src.deployment.util.ssh_deployment_client import SshDeploymentClient


class Deployment:
    def __init__(self, projectConfig, action, branch=None):
        self._git_repo = projectConfig["projectName"]
        self._git_repo = projectConfig["gitRepo"]
        self._action = action
        self._project_dir = projectConfig["projectDir"]
        self._tmp_deploy_dir = projectConfig["projectDir"] + "/.tmp_deploy_process"
        self._branch = projectConfig["defaultBranch"] if branch is None else branch
        self._ssh_deployment_client = SshDeploymentClient(projectConfig["hostName"])
        self._deployment_type = projectConfig["deploymentType"]
        self._deploy_include_list = projectConfig["deployIncludeList"]
        self._deploy_exclude_list = projectConfig["deployExcludeList"]

    @property
    def git_repo(self):
        return self._git_repo

    @git_repo.setter
    def git_repo(self, git_repo):
        self._git_repo = git_repo

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, action):
        self._action = action

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

    @ssh_deployment_client.setter
    def ssh_deployment_client(self, ssh_deployment_client):
        self._ssh_deployment_client = ssh_deployment_client

    @property
    def deployment_type(self):
        return self._deployment_type

    @deployment_type.setter
    def deployment_type(self, deployment_type):
        self._deployment_type = deployment_type

    @property
    def deploy_include_list(self):
        return self._deploy_include_list

    @deploy_include_list.setter
    def deploy_include_list(self, deploy_include_list):
        self._deploy_include_list = deploy_include_list

    @property
    def deploy_exclude_list(self):
        return self._deploy_exclude_list

    @deploy_exclude_list.setter
    def deploy_exclude_list(self, deploy_exclude_list):
        self._deploy_exclude_list = deploy_exclude_list
