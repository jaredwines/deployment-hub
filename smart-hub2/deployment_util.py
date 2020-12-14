import os
import shutil 
import re

class DeploymentUtil():

    @staticmethod
    def make_empty_dir(*target_dirs):
        for target_dir in target_dirs: 
            if os.path.isdir(target_dir): 
                shutil.rmtree(target_dir)

            os.mkdir(target_dir)

    @staticmethod
    def clone_git_repo(git_repo, branch, target_dir):
        os.system("git clone -b " + branch + " " + git_repo + " " + target_dir)

    @staticmethod
    def move_dir_contents(source_dir, target_dir, regex = ""):
        file_names = os.listdir(source_dir)
    
        for file_name in file_names:
            if not re.search(regex, file_name) : 
                shutil.move(os.path.join(source_dir, file_name), target_dir)

    @staticmethod
    def remove_dir(*target_dirs):
        for target_dir in target_dirs:
            shutil.rmtree(target_dir)