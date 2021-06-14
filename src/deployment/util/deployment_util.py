from distutils.util import strtobool


class DeploymentUtil:

    def __init__(self, deployment, ssh_deployment_client):
        self.__git_repo = deployment.git_repo
        self.__branch = deployment.branch
        self.__project_dir = deployment.project_dir
        self.__tmp_deploy_dir = deployment.tmp_deploy_dir
        self.__ssh_deployment_client = ssh_deployment_client

    def make_dir(self, *target_dirs):
        for target_dir in target_dirs:
            stdout = self.__ssh_deployment_client.exec_command(
                "if [ -d " + target_dir + " ]; then echo 'True'; else echo 'False'; fi")
            is_dir = strtobool(stdout.rstrip())

            if not is_dir:
                self.__ssh_deployment_client.exec_command("mkdir " + target_dir)

    def clone_git_repo(self, target_dir=None):
        if target_dir is None:
            target_dir = self.__project_dir

        self.__ssh_deployment_client.exec_command(
            "git clone -b " + self.__branch + " " + self.__git_repo + " " + target_dir)

    def move_deployment_contents(self, regex=".git*", source_dir=None, target_dir=None):
        if source_dir is None:
            source_dir = self.__tmp_deploy_dir

        if target_dir is None:
            target_dir = self.__project_dir

        self.__ssh_deployment_client.exec_command("rysnc --exclude '" + regex + "' " + source_dir + " " + target_dir)

    def remove_dir(self, *target_dirs):
        for target_dir in target_dirs:
            stdout = self.__ssh_deployment_client.exec_command(
                "if [ -d " + target_dir + " ]; then echo 'True'; else echo 'False'; fi")
            is_dir = strtobool(stdout.rstrip())

            if is_dir:
                self.__ssh_deployment_client.exec_command("rm -rf " + target_dir)

    def create_tmp_dir(self):
        self.remove_dir(self.__tmp_deploy_dir)
        self.make_dir(self.__tmp_deploy_dir)

    def remove_tmp_dir(self):
        self.remove_dir(self.__tmp_deploy_dir)
