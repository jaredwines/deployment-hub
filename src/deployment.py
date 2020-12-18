from abc import ABC, abstractmethod 
from os.path import expanduser
from distutils.util import strtobool
from paramiko import SSHConfig, SSHClient, RSAKey, AutoAddPolicy

class Deployment(ABC): 
    def __init__(self, host, git_repo, project_dir):
        self._host = host
        self._git_repo = git_repo
        self._project_dir = project_dir
        self._tmp_deploy_dir = expanduser("~") + "/.tmp_deploy_process"
        self._branch = "master"
        self._ssh_config = SSHConfig()
        self._ssh_client = SSHClient()
        super(Deployment, self).__init__()

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
    def ssh_config(self):
        return self._ssh_config

    @ssh_config.setter
    def ssh_config(self,ssh_config):
        self._ssh_config=ssh_config
    
    @property
    def ssh_client(self):
        return self._ssh_client

    @ssh_client.setter
    def ssh_client(self,ssh_client):
        self._ssh_client=ssh_client

    @abstractmethod
    def deploy(self):
        self.create_tmp_dir()
        self.clone_git_repo()
        self.move_deployment_contents()
        self.remove_tmp_dir()

    def start(self):
        self.exec_command("docker-compose -f " + self.project_dir + "/docker-compose.yml up -d")

    def restart(self):
        self.exec_command("docker-compose -f " + self.project_dir + "/docker-compose.yml restart")

    def stop(self):
        self.exec_command("docker-compose -f " + self.project_dir + "/docker-compose.yml stop")

    def update(self):
        self.exec_command("docker-compose -f " + self.project_dir + "/docker-compose.yml pull")
        self.exec_command("docker-compose -f " + self.project_dir + "/docker-compose.yml up -d --build homeassistant")

    def connect_ssh(self):
        self.ssh_config.parse(open("/Users/jared/.ssh/config"))
        ssh_config_properties = self.ssh_config.lookup(self.host)

        identity_file = ssh_config_properties['identityfile']
        host_name = ssh_config_properties['hostname']
        user_name = ssh_config_properties['user']

        key = RSAKey.from_private_key_file(identity_file)

        self.ssh_client.set_missing_host_key_policy(AutoAddPolicy())
        self.ssh_client.connect( hostname = host_name, username = user_name, pkey = key )

    def exec_command(self, command):
        self.ssh_client.exec_command(command)

    def make_dir(self, *target_dirs):
        for target_dir in target_dirs: 
            stdout = self.ssh_client.exec_command("if [ -d " + target_dir + " ]; then echo 'True'; else echo 'False'; fi")
            is_dir = strtobool(stdout)

            if is_dir == False: 
                self.ssh_client.exec_command("mkdir " + target_dir)

    def clone_git_repo(self, target_dir = None): 
        if target_dir == None:
            target_dir = self.project_dir
            
        self.ssh_client.exec_command("git clone -b " + self.branch + " " + self.git_repo + " " + target_dir)

    def move_deployment_contents(self, regex = ".git*", source_dir = None, target_dir = None):
        if source_dir == None :
            source_dir = self.tmp_deploy_dir

        if target_dir == None :
            target_dir = self.project_dir
            
        self.ssh_client.exec_command("rysnc --exclude '" + regex + "' " + source_dir + " " + target_dir)

    def remove_dir(self, *target_dirs):
        for target_dir in target_dirs: 
            stdout = self.ssh_client.exec_command("if [ -d " + target_dir + " ]; then echo 'True'; else echo 'False'; fi")
            is_dir = strtobool(stdout)

            if is_dir == True: 
                self.ssh_client.exec_command("rm -rf " + target_dir)

    def create_tmp_dir(self):
        self.remove_dir(self.tmp_deploy_dir)
        self.make_dir(self.tmp_deploy_dir)

    def remove_tmp_dir(self):
        self.remove_dir(self.tmp_deploy_dir)