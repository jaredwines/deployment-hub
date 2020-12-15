from deployment import Deployment
from deployment_util import DeploymentUtil
import os

class JaredWinesComDeployment(Deployment): 

    def __init__(self, branch = "master", maintenance_flag = False):
        self.maintenance_flag = maintenance_flag
        self.website_dir = "~/jaredwines.com" 
        self.host_username = "jwines"
        super().__init__("jaredwines.com", "git@github.com:jaredwines/jaredwines.com.git", branch)

    @property
    def maintenance_flag(self):
        return self.maintenance_flag

    @maintenance_flag.setter
    def maintenance_flag(self, maintenance_flag):
        self.maintenance_flag = maintenance_flag

    def configure_maintenance_mode(self, ssh_client):
        if self.maintenance_flag == True:
            os.system("sed -i 's/RewriteEngine Off/RewriteEngine On/g' ~/.htaccess")
        else:
            os.system("sed -i 's/RewriteEngine On/RewriteEngine Off/g' ~/.htaccess") 
   
    def deploy(self):  
        ssh_client = DeploymentUtil.connect_ssh(self.host, self.host_username) 

        DeploymentUtil.make_empty_dir(self.tmp_deploy_dir, self.website_dir, ssh_client)
        DeploymentUtil.clone_git_repo(self.git_repo, self.branch, self.tmp_deploy_dir, ssh_client)
        DeploymentUtil.move_dir_contents(self.tmp_deploy_dir, self.website_dir, ".git.+", ssh_client)
        DeploymentUtil.remove_dir(self.tmp_deploy_dir, ssh_client)

        self.configure_maintenance_mode(ssh_client)

        return self.branch + self.host + self.git_repo + str(self.maintenance_flag)
  