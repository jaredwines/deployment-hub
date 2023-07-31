import json
import logging

from flask import Flask
from flask_cors import CORS


from src.deployment.deployment_manager import DeploymentManager
from src.model.deployment import Deployment
from src.deployment.util.ssh_deployment_client import SshDeploymentClient



app = Flask(__name__)
CORS(app)
logging.basicConfig(format='%(message)s', level=logging.INFO)

file = open('/Users/jaredwines/Projects/deployment-hub/configuration.json')
configuration = json.load(file)

#app.logger.info(configuration)

@app.route('/project-options/', methods=['GET'])
def get_project_options():

    return True

@app.route('/<project>/<action>/', methods=['POST', 'GET'])
@app.route('/<project>/<action>/<branch>/', methods=['POST', 'GET'])
def deploy(project=None, action=None, branch=None):
    app.logger.info("deploy2")
    deployment = None
    for project_config in configuration["projects"]:
        app.logger.info(project_config)
        app.logger.info(project_config["projectName"])
        app.logger.info(project)

        if project == project_config["projectName"]:
            deployment = Deployment(project_config, action, branch)
            app.logger.info(deployment)

    if deployment is not None:
        deployment_manager = DeploymentManager(deployment)
        return deployment_manager.run()
    else:
        return "Project was not found."

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
