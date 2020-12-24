from data.deployment import Deployment
from deployment.deployment_command import DeploymentCommand
from deployment.docker_command import DockerCommand
from data.ssh_deployment_client import SshDeploymentClient
import os

class JaredWinesComDeployment(DeploymentCommand): 

    def __init__(self, branch = "master"):
        self._maintenance_flag = False

        self.__deployment = Deployment("git@github.com:jaredwines/homeassistant-config.git", branch, "/home/home-assistant")
        self.__ssh_deployment_client = SshDeploymentClient("smart-hub") 

        super().__init__(self.__deployment, self.__ssh_deployment_client ) 

    @property
    def maintenance_flag(self):
        return self._maintenance_flag

    @maintenance_flag.setter
    def maintenance_flag(self, maintenance_flag):
        self._maintenance_flag = maintenance_flag

    def configure_maintenance_mode(self):
        if self.maintenance_flag == True:
            maintenance_mode_on = "sed -i 's/RewriteEngine Off/RewriteEngine On/g' ~/.htaccess"
            self.__ssh_deployment_client.exec_command(maintenance_mode_on)
        else:
            maintenance_mode_off = "sed -i 's/RewriteEngine On/RewriteEngine Off/g' ~/.htaccess"
            self.__ssh_deployment_client.exec_command(maintenance_mode_off)

    def deploy(self):  
        self._create_tmp_dir()
        self._clone_git_repo()
        self._move_deployment_contents()
        self._remove_tmp_dir()

        self.configure_maintenance_mode()
  