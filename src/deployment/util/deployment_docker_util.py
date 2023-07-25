from distutils.util import strtobool
import sys

class DeploymentDockerUtil:

    def __init__(self, deployment):
        self.__git_repo = deployment.git_repo
        self.__branch = deployment.branch
        self.__project_dir = deployment.project_dir
        self.__tmp_deploy_dir = deployment.tmp_deploy_dir
        self.__ssh_deployment_client = deployment.ssh_deployment_client

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

        print("self.__project_dir=", self.__project_dir, file=sys.stderr)
        self.__ssh_deployment_client.exec_command(
            "docker-compose -f " + target_dir + "/docker-compose.yml stop")

    def update_docker(self, target_dir=None):
        if target_dir is None:
            target_dir = self.__project_dir

        self.__ssh_deployment_client.exec_command(
            "docker-compose -f " + target_dir + "/docker-compose.yml up -d")