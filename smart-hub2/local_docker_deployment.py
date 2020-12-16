from local_deployment import LocalDeployment
import os
import shutil 
import re

class LocalDockerDeployment(LocalDeployment): 
    def __init__(self, git_repo, project_dir):
        super().__init__(git_repo, project_dir) 

    def start(self):
        self.exec_command("docker-compose -f " + self.project_dir + "/docker-compose.yml up -d")

    def restart(self):
        self.exec_command("docker-compose -f " + self.project_dir + "/docker-compose.yml restart")

    def update(self):
        self.exec_command("docker-compose -f " + self.project_dir + "/docker-compose.yml pull")
        self.exec_command("docker-compose -f " + self.project_dir + "/docker-compose.yml up -d --build homeassistant")