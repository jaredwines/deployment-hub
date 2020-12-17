from remote_deployment import RemoteDeployment
import os

class JaredWinesComDeployment(RemoteDeployment): 

    def __init__(self):
        self._maintenance_flag = False
        super().__init__("jaredwines.com", "git@github.com:jaredwines/jaredwines.com.git", "/home/jaredw/jaredwines.com" ) 

    @property
    def maintenance_flag(self):
        return self._maintenance_flag

    @maintenance_flag.setter
    def maintenance_flag(self, maintenance_flag):
        self._maintenance_flag = maintenance_flag

    def configure_maintenance_mode(self):
        if self.maintenance_flag == True:
            maintenance_mode_on = "sed -i 's/RewriteEngine Off/RewriteEngine On/g' ~/.htaccess"
            self.exec_command(maintenance_mode_on)
        else:
            maintenance_mode_off = "sed -i 's/RewriteEngine On/RewriteEngine Off/g' ~/.htaccess"
            self.exec_command(maintenance_mode_off)

    def deploy(self):  
        super().deploy()
        self.configure_maintenance_mode()
  