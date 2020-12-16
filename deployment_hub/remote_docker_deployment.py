from remote_deployment import RemoteDeployment
from distutils.util import strtobool
from paramiko import SSHConfig, SSHClient, RSAKey, AutoAddPolicy

class RemoteDockerDeployment(RemoteDeployment): 
    def __init__(self, host, git_repo, project_dir):
        super().__init__(host, git_repo, project_dir)

    def start(self):
        self.exec_command("docker-compose -f " + self.project_dir + "/docker-compose.yml up -d")

    def restart(self):
        self.exec_command("docker-compose -f " + self.project_dir + "/docker-compose.yml restart")

    def update(self):
        self.exec_command("docker-compose -f " + self.project_dir + "/docker-compose.yml pull")
        self.exec_command("docker-compose -f " + self.project_dir + "/docker-compose.yml up -d --build homeassistant")




  