class DeploymentGitUtil:

    def __init__(self, deployment):
        self.__git_repo = deployment.git_repo
        self.__branch = deployment.branch
        self.__project_dir = deployment.project_dir
        self.__tmp_deploy_dir = deployment.tmp_deploy_dir
        self.__ssh_deployment_client = deployment.ssh_deployment_client

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

    def push_git_repo(self, target_dir=None, is_upstream_origin=True, branch=None):
        if target_dir is None:
            target_dir = self.__project_dir

        if is_upstream_origin is False:
            self.__ssh_deployment_client.exec_command(
                "git -C " + target_dir + " push --set-upstream origin " + branch)
        else:
            self.__ssh_deployment_client.exec_command(
                "git -C " + target_dir + " push")

    def clone_git_repo(self, git_repo=None, branch=None, target_dir=None):
        if target_dir is None:
            target_dir = self.__tmp_deploy_dir

        if branch is None:
            branch = self.__branch

        if git_repo is None:
            git_repo = self.__git_repo

        self.__ssh_deployment_client.exec_command(
            "git clone -b " + branch + " " + git_repo + " " + target_dir)

    def checkout_git_repo(self, target_dir=None, branch=None):
        if target_dir is None:
            target_dir = self.__tmp_deploy_dir

        if branch is None:
            branch = self.__branch

        self.__ssh_deployment_client.exec_command(
            "git -C " + target_dir + " checkout -b " + branch)
