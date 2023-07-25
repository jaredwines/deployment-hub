class DeploymentWebsiteUtil:

    def __init__(self, deployment):
        self.__git_repo = deployment.git_repo
        self.__branch = deployment.branch
        self.__project_dir = deployment.project_dir
        self.__tmp_deploy_dir = deployment.tmp_deploy_dir
        self.__ssh_deployment_client = deployment.ssh_deployment_client
        self._maintenance_flag = False

    @property
    def maintenance_flag(self):
        return self._maintenance_flag

    @maintenance_flag.setter
    def maintenance_flag(self, maintenance_flag):
        self._maintenance_flag = maintenance_flag

    def configure_maintenance_mode(self):
        if self.maintenance_flag:
            maintenance_mode_on = "sed -i 's/RewriteEngine Off/RewriteEngine On/g' ~/.htaccess"
            self.__ssh_deployment_client.exec_command(maintenance_mode_on)
        else:
            maintenance_mode_off = "sed -i 's/RewriteEngine On/RewriteEngine Off/g' ~/.htaccess"
            self.__ssh_deployment_client.exec_command(maintenance_mode_off)

    # def deploy(self):
    #     self._deployment_util.create_tmp_dir()
    #     self._deployment_util.clone_git_repo()
    #     self._deployment_util.move_deployment_contents()
    #     self._deployment_util.remove_tmp_dir()
