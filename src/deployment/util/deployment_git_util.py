from distutils.util import strtobool


class DeploymentGitUtil:

    def __init__(self, deployment, ssh_deployment_client):
        self.__git_repo = deployment.git_repo
        self.__branch = deployment.branch
        self.__project_dir = deployment.project_dir
        self.__tmp_deploy_dir = deployment.tmp_deploy_dir
        self.__ssh_deployment_client = ssh_deployment_client

    def pull_git_repo(self, target_dir=None):
        if target_dir is None:
            target_dir = self.__project_dir

        self.__ssh_deployment_client.exec_command(
            "git -C " + target_dir + " pull")

    def add_git_repo(self, target_dir=None):
        if target_dir is None:
            target_dir = self.__project_dir

        self.__ssh_deployment_client.exec_command(
            "git -C " + target_dir + " add --all")

    def commit_git_repo(self, target_dir=None):
        if target_dir is None:
            target_dir = self.__project_dir

        self.__ssh_deployment_client.exec_command(
            "git -C " + target_dir + " commit -m \"Backup.\"")

    def push_git_repo(self, target_dir=None):
        if target_dir is None:
            target_dir = self.__project_dir

        self.__ssh_deployment_client.exec_command(
            "git -C " + target_dir + " push")

    def clone_git_repo(self, target_dir=None):
        if target_dir is None:
            target_dir = self.__tmp_deploy_dir

        self.__ssh_deployment_client.exec_command(
            "git clone -b " + self.__branch + " " + self.__git_repo + " " + target_dir)
