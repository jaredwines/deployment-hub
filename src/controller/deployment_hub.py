import json
import logging

from flask import Flask
from flask_cors import CORS

from src.deployment.deployment_manager import DeploymentManager
from src.model.deployment import Deployment

app = Flask(__name__)
CORS(app)
logging.basicConfig(format='%(message)s', level=logging.INFO)

file = open('/usr/src/deployment-hub/configuration.json')
configuration = json.load(file)


# app.logger.info(configuration)

@app.route('/project-options/', methods=['GET'])
def get_project_options():
    return True


@app.route('/<project>/<action>/', methods=['POST', 'GET'])
@app.route('/<project>/<action>/<branch>/', methods=['POST', 'GET'])
def deploy(project=None, action=None, branch=None):
    deployment = None
    for project_config in configuration["projects"]:

        if project == project_config["projectName"]:
            deployment = Deployment(project_config, action, branch)
            app.logger.info(deployment)

    if deployment is not None:
        deployment_manager = DeploymentManager(deployment)
        return json.dump(deployment_manager.run())
    else:
        return ["Project was not found!"]


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
