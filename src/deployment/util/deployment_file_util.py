from distutils.util import strtobool

from src.deployment.util.deployment_git_util import DeploymentGitUtil


class DeploymentFileUtil(DeploymentGitUtil):

    def __init__(self, deployment):
        self.__git_repo = deployment.git_repo
        self.__branch = deployment.branch
        self.__project_dir = deployment.project_dir
        self.__tmp_deploy_dir = deployment.tmp_deploy_dir
        self.__ssh_deployment_client = deployment.ssh_deployment_client
        DeploymentGitUtil.__init__(self, deployment)

    def make_dir(self, *target_dirs):
        for target_dir in target_dirs:
            stdout = self.__ssh_deployment_client.exec_command(
                "if [ -d " + target_dir + " ]; then echo 'True'; else echo 'False'; fi")
            is_dir = strtobool(stdout.rstrip())

            if not is_dir:
                self.__ssh_deployment_client.exec_command("mkdir " + target_dir)

    def move_deployment_contents(self, regex_exclude=".git", regex_include=None, source_dir=None, target_dir=None, ):
        if source_dir is None:
            source_dir = self.__tmp_deploy_dir

        if target_dir is None:
            target_dir = self.__project_dir

        if regex_include is None:
            self.__ssh_deployment_client.exec_command("rsync -a --exclude " + regex_exclude + " " + source_dir + "/* " + target_dir)
        else:
            self.__ssh_deployment_client.exec_command("rsync -a --exclude " + regex_exclude + " --include " + regex_include + " " + source_dir + "/* " + target_dir)

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

    def deploy(self, regex_exclude=".git",  regex_include=None, source_dir=None, target_dir=None):
        self.create_tmp_dir()
        self.clone_git_repo()
        self.move_deployment_contents(regex_exclude, regex_include, source_dir, target_dir)
        self.remove_tmp_dir()
