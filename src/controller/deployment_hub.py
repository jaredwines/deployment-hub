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


@app.route('/<project>/<action>/', methods=['POST', 'GET'])
@app.route('/<project>/<action>/<branch>/', methods=['POST', 'GET'])
def deploy(project=None, branch=None, action=None):
    if project == "alohamillworks":
        if branch is None:
            aloha_millworks = AlohaMillworksDeployment("main")
        else:
            aloha_millworks = AlohaMillworksDeployment(branch)

        if action == "deploy":
            return aloha_millworks.deploy()

        elif action == "backup":
            return aloha_millworks.backup()

        # if action == "maintenance-mode":
        #     aloha_millworks.maintenance_flag = "True"
        #     return aloha_millworks.deploy()

    if project == "coastalteardrops":
        if branch is None:
            coastal_teardrops = CoastalTeardropsDeployment("main")
        else:
            coastal_teardrops = CoastalTeardropsDeployment(branch)

        if action == "deploy":
            return coastal_teardrops.deploy()

        elif action == "backup":
            return coastal_teardrops.backup()

        # if action == "maintenance-mode":
        #     coastal_teardrops.maintenance_flag = "True"
        #     return coastal_teardrops.deploy()

    if project == "jaredwines":
        if branch is None:
            jared_wines = JaredWinesComDeployment()
        else:
            jared_wines = JaredWinesComDeployment(branch)

        if action == "deploy":
            return jared_wines.deploy()

        elif action == "backup":
            return jared_wines.backup()

        # if action == "maintenance-mode":
        #     jared_wines_com.maintenance_flag = "True"
        #     return jared_wines_com.deploy()

    if project == "home-assistant":
        if branch is None:
            home_assistant = HomeAssistantDeployment()
        else:
            home_assistant = HomeAssistantDeployment(branch)

        if action == "deploy":
            return home_assistant.deploy()

        elif action == "start":
            return home_assistant.start_docker()

        elif action == "stop":
            return home_assistant.stop_docker()

        elif action == "restart":
            return home_assistant.restart_docker()

        elif action == "update":
            return home_assistant.update_docker()

        elif action == "backup":
            return home_assistant.backup()

    if project == "homebridge":
        if branch is None:
            homebridge = HomebridgeDeployment()
        else:
            homebridge = HomebridgeDeployment(branch)

        if action == "deploy":
            return homebridge.deploy()

        elif action == "start":
            return homebridge.start_docker()

        elif action == "stop":
            return homebridge.stop_docker()

        elif action == "restart":
            return homebridge.restart_docker()

        elif action == "update":
            return homebridge.update_docker()

        elif action == "backup":
            return homebridge.backup()

    if project == "deployment-hub":
        if branch is None:
            deployment_hub = DeploymentHubDeployment()
        else:
            deployment_hub = DeploymentHubDeployment(branch)

        if action == "deploy":
            return deployment_hub.update_docker()

        elif action == "start":
            return deployment_hub.start_docker()

        elif action == "stop":
            return deployment_hub.stop_docker()

        elif action == "restart":
            return deployment_hub.restart_docker()

        elif action == "backup":
            return deployment_hub.backup()

    if project == "deployment-hub-ui":
        if branch is None:
            deployment_hub_ui = DeploymentHubUIDeployment()
        else:
            deployment_hub_ui = DeploymentHubUIDeployment(branch)

        if action == "deploy":
            return deployment_hub_ui.deploy()

        elif action == "start":
            return deployment_hub_ui.start_docker()

        elif action == "stop":
            return deployment_hub_ui.stop_docker()

        elif action == "restart":
            return deployment_hub_ui.restart_docker()

        elif action == "update":
            return deployment_hub_ui.update_docker()

        elif action == "backup":
            return deployment_hub_ui.backup()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
