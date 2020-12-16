from deployment import Deployment
from distutils.util import strtobool
from paramiko import SSHConfig, SSHClient, RSAKey, AutoAddPolicy

class RemoteDeployment(Deployment): 
    def __init__(self, host, git_repo, project_dir):
        self._ssh_config = SSHConfig()
        self._ssh_client = SSHClient()
        super().__init__(host, git_repo, project_dir)

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

    def deploy(self):
        self.create_tmp_dir()
        self.clone_git_repo()
        self.move_deployment_contents()
        self.remove_tmp_dir()

  