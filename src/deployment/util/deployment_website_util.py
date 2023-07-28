from src.deployment.util.deployment_file_util import DeploymentFileUtil


class DeploymentWebsiteUtil(DeploymentFileUtil):

    def __init__(self, deployment):
        self.__git_repo = deployment.git_repo
        self.__branch = deployment.branch
        self.__project_dir = deployment.project_dir
        self.__tmp_deploy_dir = deployment.tmp_deploy_dir
        self.__ssh_deployment_client = deployment.ssh_deployment_client
        self._maintenance_flag = False
        DeploymentFileUtil.__init__(self, deployment)

    @property
    def maintenance_flag(self):
        return self._maintenance_flag

    @maintenance_flag.setter
    def maintenance_flag(self, maintenance_flag):
        self._maintenance_flag = maintenance_flag

    def configure_maintenance_mode(self):
        if self.maintenance_flag:
            maintenance_mode_on = "sed -i 's/RewriteEngine Off/RewriteEngine On/g' ~/.htaccess"
            return self.__ssh_deployment_client.exec_command(maintenance_mode_on)
        else:
            maintenance_mode_off = "sed -i 's/RewriteEngine On/RewriteEngine Off/g' ~/.htaccess"
            return self.__ssh_deployment_client.exec_command(maintenance_mode_off)

    def deploy(self):
        res = self.create_tmp_dir()
        res += self.clone_git_repo()
        res += self.move_deployment_contents()
        res += self.remove_tmp_dir()

        self.configure_maintenance_mode()
