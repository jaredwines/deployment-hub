from src.deployment.util.deployment_util import DeploymentUtil
from src.deployment.util.ssh_deployment_client import SshDeploymentClient
from src.model.deployment import Deployment


class JaredWinesComDeployment:

    def __init__(self, branch="main"):
        self._maintenance_flag = False
        self.__deployment = Deployment("git@github.com:jaredwines/jaredwines.com.git", branch,
                                       "/home/dh_agtzej/jaredwines.com")
        self.__ssh_deployment_jaredwines = SshDeploymentClient("jaredwines")
        self._deployment_util = DeploymentUtil(self.__deployment, self.__ssh_deployment_jaredwines)

    @property
    def maintenance_flag(self):
        return self._maintenance_flag

    @maintenance_flag.setter
    def maintenance_flag(self, maintenance_flag):
        self._maintenance_flag = maintenance_flag

    def configure_maintenance_mode(self):
        if self.maintenance_flag:
            maintenance_mode_on = "sed -i 's/RewriteEngine Off/RewriteEngine On/g' ~/.htaccess"
            self.__ssh_deployment_jaredwines.exec_command(maintenance_mode_on)
        else:
            maintenance_mode_off = "sed -i 's/RewriteEngine On/RewriteEngine Off/g' ~/.htaccess"
            self.__ssh_deployment_jaredwines.exec_command(maintenance_mode_off)

    def deploy(self):
        self._deployment_util.create_tmp_dir()
        self._deployment_util.clone_git_repo()
        self._deployment_util.move_deployment_contents()
        self._deployment_util.remove_tmp_dir()

        #self.configure_maintenance_mode()
