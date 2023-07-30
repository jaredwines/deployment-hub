import json
import logging

from flask import Flask

from src.deployment.aloha_millworks_com_deployment import AlohaMillworksDeployment
from src.deployment.coastal_teardrops_com_deployment import CoastalTeardropsDeployment
from src.deployment.deployment_hub_deployment import DeploymentHubDeployment
from src.deployment.deployment_hub_ui_deployment import DeploymentHubUIDeployment
from src.deployment.home_assistant_deployment import HomeAssistantDeployment
from src.deployment.homebridge_deployment import HomebridgeDeployment
from src.deployment.jared_wines_com_deployment import JaredWinesComDeployment

app = Flask(__name__)
logging.basicConfig(format='%(message)s', level=logging.INFO)


@app.route('/project-options/', methods=['GET'])
def get_project_options():
    return True


def jsonify(response):
    return json.dumps(response)


@app.route('/<project>/<action>/', methods=['POST', 'GET'])
@app.route('/<project>/<action>/<branch>/', methods=['POST', 'GET'])
def deploy(project=None, branch=None, action=None):
    if project == "alohamillworks":
        if branch is None:
            aloha_millworks = AlohaMillworksDeployment("main")
        else:
            aloha_millworks = AlohaMillworksDeployment(branch)

        if action == "deploy":
            return jsonify(aloha_millworks.deploy())

        elif action == "backup":
            return jsonify(aloha_millworks.backup())

        # if action == "maintenance-mode":
        #     aloha_millworks.maintenance_flag = "True"
        #     return jsonify(aloha_millworks.deploy()

    if project == "coastalteardrops":
        if branch is None:
            coastal_teardrops = CoastalTeardropsDeployment("main")
        else:
            coastal_teardrops = CoastalTeardropsDeployment(branch)

        if action == "deploy":
            return jsonify(coastal_teardrops.deploy())

        elif action == "backup":
            return jsonify(coastal_teardrops.backup())

        # if action == "maintenance-mode":
        #     coastal_teardrops.maintenance_flag = "True"
        #     return jsonify(coastal_teardrops.deploy()

    if project == "jaredwines":
        if branch is None:
            jared_wines = JaredWinesComDeployment()
        else:
            jared_wines = JaredWinesComDeployment(branch)

        if action == "deploy":
            return jsonify(jared_wines.deploy())

        elif action == "backup":
            return jsonify(jared_wines.backup())

        # if action == "maintenance-mode":
        #     jared_wines_com.maintenance_flag = "True"
        #     return jsonify(jared_wines_com.deploy()

    if project == "home-assistant":
        if branch is None:
            home_assistant = HomeAssistantDeployment()
        else:
            home_assistant = HomeAssistantDeployment(branch)

        if action == "deploy":
            return jsonify(home_assistant.deploy())

        elif action == "start":
            return jsonify(home_assistant.start_docker())

        elif action == "stop":
            return jsonify(home_assistant.stop_docker())

        elif action == "restart":
            return jsonify(home_assistant.restart_docker())

        elif action == "update":
            return jsonify(home_assistant.update_docker())

        elif action == "backup":
            return jsonify(home_assistant.backup())

    if project == "homebridge":
        if branch is None:
            homebridge = HomebridgeDeployment()
        else:
            homebridge = HomebridgeDeployment(branch)

        if action == "deploy":
            return jsonify(homebridge.deploy())

        elif action == "start":
            return jsonify(homebridge.start_docker())

        elif action == "stop":
            return jsonify(homebridge.stop_docker())

        elif action == "restart":
            return jsonify(homebridge.restart_docker())

        elif action == "update":
            return jsonify(homebridge.update_docker())

        elif action == "backup":
            return jsonify(homebridge.backup())

    if project == "deployment-hub":
        if branch is None:
            deployment_hub = DeploymentHubDeployment()
        else:
            deployment_hub = DeploymentHubDeployment(branch)

        if action == "deploy":
            return jsonify(deployment_hub.deploy())

        elif action == "start":
            return jsonify(deployment_hub.start_docker())

        elif action == "stop":
            return jsonify(deployment_hub.stop_docker())

        elif action == "restart":
            return jsonify(deployment_hub.restart_docker())

        elif action == "update":
            return jsonify(deployment_hub.update_docker())

        elif action == "backup":
            return jsonify(deployment_hub.backup())

    if project == "deployment-hub-ui":
        if branch is None:
            deployment_hub_ui = DeploymentHubUIDeployment()
        else:
            deployment_hub_ui = DeploymentHubUIDeployment(branch)

        if action == "deploy":
            return jsonify(deployment_hub_ui.deploy())

        elif action == "start":
            return jsonify(deployment_hub_ui.start_docker())

        elif action == "stop":
            return jsonify(deployment_hub_ui.stop_docker())

        elif action == "restart":
            return jsonify(deployment_hub_ui.restart_docker())

        elif action == "update":
            return jsonify(deployment_hub_ui.update_docker())

        elif action == "backup":
            return jsonify(deployment_hub_ui.backup())


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
