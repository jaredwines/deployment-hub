from abc import ABC, abstractmethod


class DockerCommand(ABC):
    def __init__(self, deployment, ssh_deployment):
        self.git_repo = deployment.git_repo
        self.project_dir = deployment.project_dir
        self.branch = deployment.branch
        self._ssh_client = ssh_deployment

    @abstractmethod
    def start_docker(self):
        pass

    @abstractmethod
    def restart_docker(self):
        pass

    @abstractmethod
    def stop_docker(self):
        pass

    @abstractmethod
    def update_docker(self):
        pass

    def execute_docker_command(self, command):
        self.__ssh_deployment_client.exec_command(command)
