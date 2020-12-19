from deployment import Deployment
import sys

class HomeAssistantDeployment(Deployment): 

    def __init__(self):
        super().__init__("smart-hub", "git@github.com:jaredwines/homeassistant-config.git", "/home/home-assistant")

    def start(self):
        self._exec_command("docker-compose -f " + self.project_dir + "/docker-compose.yml up -d")

    def restart(self):
        self._exec_command("docker-compose -f " + self.project_dir + "/docker-compose.yml restart") 

    def stop(self):
        self._exec_command("docker-compose -f " + self.project_dir + "/docker-compose.yml stop")

    def update(self):
        self._exec_command("docker-compose -f " + self.project_dir + "/docker-compose.yml pull")
        self._exec_command("docker-compose -f " + self.project_dir + "/docker-compose.yml up -d --build homeassistant")
   
    def deploy(self):
        self._create_tmp_dir()
        self._clone_git_repo()
        self._move_deployment_contents()
        self._remove_tmp_dir()
        
        self.restart()

  