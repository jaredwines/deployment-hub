from src.deployment.util.deployment_file_util import DeploymentFileUtil


class DeploymentWebsiteUtil(DeploymentFileUtil):

    def __init__(self, deployment):
        self.__git_repo = deployment.git_repo
        self.__branch = deployment.branch
        self.__project_dir = deployment.project_dir
        self.__tmp_deploy_dir = deployment.tmp_deploy_dir
        self.__ssh_deployment_client = deployment.ssh_deployment_client
        self.__deploy_include_list = deployment.deploy_include_list
        self.__deploy_exclude_list = deployment.deploy_exclude_list
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

    def deploy(self, include_list=None, exclude_list=None, source_dir=None, target_dir=None):
        if self.__deploy_include_list is not None:
            include_list = self.__deploy_include_list

        if self.__deploy_include_list is not None:
            include_list = self.__deploy_include_list

        return DeploymentFileUtil.deploy(self, include_list, exclude_list, source_dir, target_dir)
        #self.configure_maintenance_mode()
