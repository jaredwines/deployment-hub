from abc import ABC, abstractmethod


class DockerCommand(ABC):
    def __init__(self, deployment, ssh_deployment):
        self.git_repo = deployment.git_repo
        self.project_dir = deployment.project_dir
        self.branch = deployment.branch
        self._ssh_client = ssh_deployment

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
