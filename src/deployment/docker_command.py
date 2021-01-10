from abc import ABC, abstractmethod 
from ..model.deployment import Deployment
from ..model.ssh_deployment_client import SshDeploymentClient
import sys
import time

class DockerCommand(ABC): 
    def __init__(self, deployment, ssh_deployment):
        self.__git_repo = deployment.git_repo
        self.__project_dir = deployment.project_dir
        self.__branch = deployment.branch
        self.__ssh_client = deployment.ssh_client 


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