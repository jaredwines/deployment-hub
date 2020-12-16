from deployment import Deployment
import os
import shutil 
import re

class LocalDeployment(Deployment): 
    def __init__(self, git_repo, project_dir):
        super().__init__("smart-hub", git_repo, project_dir) 

    def make_dir(self, *target_dirs):
        for target_dir in target_dirs: 
           os.mkdir(target_dir)

    def clone_git_repo(self, target_dir = None): 
        if target_dir == None :
            target_dir = self.project_dir
           
        os.system("git clone -b " + self.branch + " " + self.git_repo + " " + target_dir)

    def move_deployment_contents(self, source_dir = None, target_dir = None, regex = ".git*"):
        if source_dir == None :
            source_dir = self.tmp_deploy_dir

        if target_dir == None :
            target_dir = self.project_dir

        os.system("rysnc --exclude '" + regex + "' " + source_dir + " " + target_dir)

    def remove_dir(self, *target_dirs):
        for target_dir in target_dirs:
            shutil.rmtree(target_dir)
        
    def create_tmp_dir(self):
        self.remove_dir(self.tmp_deploy_dir)
        self.make_dir(self.tmp_deploy_dir)

    def remove_tmp_dir(self):
        self.remove_dir(self.tmp_deploy_dir)

    def deploy(self):
        self.create_tmp_dir()
        self.clone_git_repo()
        self.move_deployment_contents()
        self.remove_tmp_dir()
         