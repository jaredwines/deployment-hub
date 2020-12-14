from deployment import Deployment
from deployment_util import DeploymentUtil
import os

class JaredWinesComDeployment(Deployment): 

    def __init__(self, branch = "master", maintenance_flag = False):
        self._host = "jaredwines.com"
        self._git_repo = "git@github.com:jaredwines/jaredwines.com.git"
        self.maintenance_flag = maintenance_flag
        self.home_dir = os.path.expanduser("~")
        self.tmp_deploy_dir= home_dir + "/.tmp_process_deploy_www.jaredwines.com"
        self.website_dir=home_dir + "/jaredwines.com" 
        super().__init__(self._host, self._git_repo, branch)

    @property
    def maintenance_flag(self):
        return self.maintenance_flag

    @maintenance_flag.setter
    def maintenance_flag(self, maintenance_flag):
        self.maintenance_flag = maintenance_flag

    def configure_maintenance_mode(self):
        if self.maintenance_flag == True:
            os.system("sed -i 's/RewriteEngine Off/RewriteEngine On/g' " + self.home_dir + "/.htaccess")
        else:
            os.system("sed -i 's/RewriteEngine On/RewriteEngine Off/g' " + self.home_dir + "/.htaccess")
   
    def deploy(self):  
        home_dir = os.path.expanduser("~")
        tmp_deploy_dir= home_dir + "/.tmp_process_deploy_www.jaredwines.com"
        website_dir=home_dir + "/jaredwines.com" 

        DeploymentUtil.make_empty_dir(tmp_deploy_dir, website_dir)
        DeploymentUtil.clone_git_repo(self.git_repo, self.branch, tmp_deploy_dir)
        DeploymentUtil.move_dir_contents(tmp_deploy_dir, website_dir, ".git.+")
        DeploymentUtil.remove_dir(tmp_deploy_dir)

        self.configure_maintenance_mode

        return self.branch + self.host + self.git_repo + str(self.maintenance_flag)
  