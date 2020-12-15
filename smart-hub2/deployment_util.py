import os
import shutil 
import re
import paramiko

class DeploymentUtil():

    @staticmethod
    def connect_ssh(host, user):
        key = paramiko.RSAKey.from_private_key_file("/home/jared/.ssh/id_rsa_smart_hub")
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh_client.connect( hostname = host, username = user, pkey = key )

        return ssh_client

    @staticmethod
    def make_empty_dir(*target_dirs, ssh_client = None):
        
        for target_dir in target_dirs: 
            if os.path.isdir(target_dir): 
                shutil.rmtree(target_dir)

            os.mkdir(target_dir)

    @staticmethod
    def clone_git_repo(host, git_repo, branch, target_dir, ssh_client = None):
        os.system("git clone -b " + branch + " " + git_repo + " " + target_dir)
      

    @staticmethod
    def move_dir_contents(source_dir, target_dir, regex = "", ssh_client = None):
        file_names = os.listdir(source_dir)
    
        for file_name in file_names:
            if not re.search(regex, file_name) : 
                shutil.move(os.path.join(source_dir, file_name), target_dir)

    @staticmethod
    def remove_dir(*target_dirs, ssh_client = None):
        for target_dir in target_dirs:
            shutil.rmtree(target_dir)