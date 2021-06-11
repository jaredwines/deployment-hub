from src.deployment.util.deployment_command import DeploymentCommand
from src.deployment.util.ssh_deployment_client import SshDeploymentClient
from src.model.deployment import Deployment


class JaredWinesComDeployment(DeploymentCommand):

    def __init__(self, branch="master"):
        self._maintenance_flag = False

        self.__deployment = Deployment("git@github.com:jaredwines/jaredwines.com.git", branch,
                                       "/home/home-assistant")
        self.__ssh_deployment_client = SshDeploymentClient("jaredwines.com")

        super().__init__(self.__deployment, self.__ssh_deployment_client)

    @property
    def maintenance_flag(self):
        return self._maintenance_flag

    @maintenance_flag.setter
    def maintenance_flag(self, maintenance_flag):
        self._maintenance_flag = maintenance_flag

    def configure_maintenance_mode(self):
        if self.maintenance_flag == True:
            maintenance_mode_on = "sed -i 's/RewriteEngine Off/RewriteEngine On/g' ~/.htaccess"
            self.execute_deployment_command()
            self.execute_deployment_command(maintenance_mode_on)
        else:
            maintenance_mode_off = "sed -i 's/RewriteEngine On/RewriteEngine Off/g' ~/.htaccess"
            self.execute_deployment_command(maintenance_mode_off)

    def deploy(self):
        self._create_tmp_dir()
        self._clone_git_repo()
        self._move_deployment_contents()
        self._remove_tmp_dir()

        self.configure_maintenance_mode()
