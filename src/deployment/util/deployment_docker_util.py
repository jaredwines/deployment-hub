from src.deployment.util.deployment_file_util import DeploymentFileUtil


class DeploymentDockerUtil(DeploymentFileUtil):

    def __init__(self, deployment):
        self.__git_repo = deployment.git_repo
        self.__branch = deployment.branch
        self.__project_dir = deployment.project_dir
        self.__tmp_deploy_dir = deployment.tmp_deploy_dir
        self.__ssh_deployment_client = deployment.ssh_deployment_client
        self.__deploy_include_list = deployment.deploy_include_list
        self.__deploy_exclude_list = deployment.deploy_exclude_list
        DeploymentFileUtil.__init__(self, deployment)

    def start_docker(self, target_dir=None):
        if target_dir is None:
            target_dir = self.__project_dir

        return self.__ssh_deployment_client.exec_command(
            "docker-compose -f " + target_dir + "/docker-compose.yml start")

    def restart_docker(self, target_dir=None):
        if target_dir is None:
            target_dir = self.__project_dir

        return self.__ssh_deployment_client.exec_command(
            "docker-compose -f " + target_dir + "/docker-compose.yml restart")

    def stop_docker(self, target_dir=None):
        if target_dir is None:
            target_dir = self.__project_dir

        return self.__ssh_deployment_client.exec_command(
            "docker-compose -f " + target_dir + "/docker-compose.yml stop")

    def update_docker(self, target_dir=None):
        if target_dir is None:
            target_dir = self.__project_dir

        is_file = self.__ssh_deployment_client.exec_command_is_file(self.__project_dir + "/.env")

        res = []
        if is_file:
            res += self.__ssh_deployment_client.exec_command(
                "sed -i '/BRANCH/c\BRANCH=" + self.__branch + "' " +
                self.__project_dir + "/.env")

        res += self.__ssh_deployment_client.exec_command(
            "docker-compose --file " + target_dir + "/docker-compose.yml up --force-recreate --build -d")
        return res

    def deploy(self, include_list=None, exclude_list=None, source_dir=None, target_dir=None):
        if self.__deploy_include_list is not None:
            include_list = self.__deploy_include_list

        if self.__deploy_include_list is not None:
            include_list = self.__deploy_include_list

        res = DeploymentFileUtil.deploy(self, include_list, exclude_list, source_dir, target_dir)
        res += self.update_docker()

        return res
