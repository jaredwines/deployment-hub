from abc import ABC, abstractmethod 
from os.path import expanduser
from distutils.util import strtobool
from paramiko import SSHConfig, SSHClient, RSAKey, AutoAddPolicy
import sys
import time

class Deployment(ABC): 
    def __init__(self, host, git_repo, project_dir):
        self._host = host
        self._git_repo = git_repo
        self._project_dir = project_dir
        self._tmp_deploy_dir = expanduser("~") + "/.tmp_deploy_process"
        self._branch = "master"
        self._ssh_client = self.__create_ssh_client()
        super().__init__()

    def __del__(self):
        self.ssh_client.close()

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self,host):
        self._host=host

    @property
    def git_repo(self):
        return self._git_repo
    
    @git_repo.setter
    def git_repo(self,git_repo):
        self._git_repo=git_repo

    @property
    def tmp_deploy_dir(self):
        return self._tmp_deploy_dir
    
    @tmp_deploy_dir.setter
    def tmp_deploy_dir(self,tmp_deploy_dir):
        self._tmp_deploy_dir=tmp_deploy_dir

    @property
    def project_dir(self):
        return self._project_dir
    
    @project_dir.setter
    def project_dir(self,project_dir):
        self._project_dir=project_dir

    @property
    def branch(self):
        return self._branch
    
    @branch.setter
    def branch(self,branch):
        self._branch=branch
    
    @property
    def ssh_client(self):
        return self._ssh_client

    @ssh_client.setter
    def ssh_client(self,ssh_client):
        self._ssh_client=ssh_client

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def restart(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def deploy(self):
        pass

    def __create_ssh_client(self):
        ssh_client = SSHClient()
        ssh_config = SSHConfig()
        ssh_config.parse(open(expanduser("~") + "/.ssh/config"))
        ssh_config_properties = ssh_config.lookup(self.host)

        identity_file = ssh_config_properties['identityfile'][0]
        host_name = ssh_config_properties['hostname']
        user_name = ssh_config_properties['user']

        key = RSAKey.from_private_key_file(identity_file)
 
        ssh_client.set_missing_host_key_policy(AutoAddPolicy())
        ssh_client.connect( hostname = host_name, username = user_name, pkey = key )

        return ssh_client

    def _exec_command(self, command):
        print(command, file=sys.stderr)
        print('Hello world!exute command', file=sys.stderr)
        stdin, stdout, stderr = self.ssh_client.exec_command(command)
        while int(stdout.channel.recv_exit_status()) != 0: time.sleep(1)
        
        output = ""
        for line in stdout:
            output=output+line

        return output

    def _make_dir(self, *target_dirs):
        for target_dir in target_dirs: 
            stdout = self._exec_command("if [ -d " + target_dir + " ]; then echo 'True'; else echo 'False'; fi")
            is_dir = strtobool(stdout)

            if is_dir == False: 
                self._exec_command("mkdir " + target_dir)

    def _clone_git_repo(self, target_dir = None): 
        if target_dir == None:
            target_dir = self.project_dir
            
        self._exec_command("git clone -b " + self.branch + " " + self.git_repo + " " + target_dir)

    def _move_deployment_contents(self, regex = ".git*", source_dir = None, target_dir = None):
        if source_dir == None :
            source_dir = self.tmp_deploy_dir

        if target_dir == None :
            target_dir = self.project_dir
            
        self._exec_command("rysnc --exclude '" + regex + "' " + source_dir + " " + target_dir)

    def _remove_dir(self, *target_dirs):
        for target_dir in target_dirs: 
            stdout = self._exec_command("if [ -d " + target_dir + " ]; then echo 'True'; else echo 'False'; fi")
            is_dir = strtobool(stdout)

            if is_dir == True: 
                self._exec_command("rm -rf " + target_dir)

    def _create_tmp_dir(self):
        self._remove_dir(self.tmp_deploy_dir)
        self._make_dir(self.tmp_deploy_dir)

    def _remove_tmp_dir(self):
        self._remove_dir(self.tmp_deploy_dir)