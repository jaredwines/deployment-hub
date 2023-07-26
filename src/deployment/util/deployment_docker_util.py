import sys

from src.deployment.util.deployment_file_util import DeploymentFileUtil


class DeploymentDockerUtil(DeploymentFileUtil):

    def __init__(self, deployment):
        self.__git_repo = deployment.git_repo
        self.__branch = deployment.branch
        self.__project_dir = deployment.project_dir
        self.__tmp_deploy_dir = deployment.tmp_deploy_dir
        self.__ssh_deployment_client = deployment.ssh_deployment_client
        DeploymentFileUtil.__init__(self, deployment)

    def start_docker(self, target_dir=None):
        if target_dir is None:
            target_dir = self.__project_dir

        self.__ssh_deployment_client.exec_command(
            "docker-compose -f " + target_dir + "/docker-compose.yml start")

    def restart_docker(self, target_dir=None):
        if target_dir is None:
            target_dir = self.__project_dir

        self.__ssh_deployment_client.exec_command(
            "docker-compose -f " + target_dir + "/docker-compose.yml restart")

    def stop_docker(self, target_dir=None):
        if target_dir is None:
            target_dir = self.__project_dir

        self.__ssh_deployment_client.exec_command(
            "docker-compose -f " + target_dir + "/docker-compose.yml stop")

    def update_docker(self, target_dir=None):
        if target_dir is None:
            target_dir = self.__project_dir

        self.__ssh_deployment_client.exec_command(
            "sed -i '/BRANCH/c\BRANCH=" + self.__branch + "' " +
            self.__project_dir + "/.env")
        self.__ssh_deployment_client.exec_command(
            "docker-compose --file " + target_dir + "/docker-compose.yml up --force-recreate --build -d")

    def backup(self):
        self.add_git_repo()
        self.commit_git_repo()
        self.push_git_repo()
