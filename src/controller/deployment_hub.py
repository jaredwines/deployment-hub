from flask import Flask, Response

from src.deployment.aloha_millworks_com_deployment import AlohaMillworksDeployment
from src.deployment.coastal_teardrops_com_deployment import CoastalTeardropsDeployment
from src.deployment.deployment_hub_deployment import DeploymentHubDeployment
from src.deployment.deployment_hub_ui_deployment import DeploymentHubUIDeployment
from src.deployment.home_assistant_deployment import HomeAssistantDeployment
from src.deployment.homebridge_deployment import HomebridgeDeployment
from src.deployment.jared_wines_com_deployment import JaredWinesComDeployment

app = Flask(__name__)


@app.route('/<project>/<action>/', methods=['POST', 'GET'])
@app.route('/<project>/<action>/<branch>/', methods=['POST', 'GET'])
def deploy(project=None, branch=None, action=None):
    if project == "alohamillworks":
        if branch is None:
            aloha_millworks = AlohaMillworksDeployment("main")
        else:
            aloha_millworks = AlohaMillworksDeployment(branch)

        if action == "deploy":
            return Response(aloha_millworks.deploy(), mimetype='text/plain')

        # if action == "maintenance-mode":
        #     aloha_millworks.maintenance_flag = "True"
        #     return Response(aloha_millworks.deploy(), mimetype='text/plain')

    if project == "coastalteardrops":
        if branch is None:
            coastal_teardrops = CoastalTeardropsDeployment("main")
        else:
            coastal_teardrops = CoastalTeardropsDeployment(branch)

        if action == "deploy":
            return Response(coastal_teardrops.deploy(), mimetype='text/plain')

        # if action == "maintenance-mode":
        #     coastal_teardrops.maintenance_flag = "True"
        #     return Response(coastal_teardrops.deploy(), mimetype='text/plain')

    if project == "jaredwines":
        if branch is None:
            jared_wines = JaredWinesComDeployment()
        else:
            jared_wines = JaredWinesComDeployment(branch)

        if action == "deploy":
            return Response(jared_wines.deploy(), mimetype='text/plain')

        # if action == "maintenance-mode":
        #     jared_wines_com.maintenance_flag = "True"
        #     return Response(jared_wines_com.deploy(), mimetype='text/plain')

    if project == "home-assistant":
        if branch is None:
            home_assistant = HomeAssistantDeployment()
        else:
            home_assistant = HomeAssistantDeployment(branch)

        if action == "deploy":
            return Response(home_assistant.deploy(), mimetype='text/plain')

        elif action == "start":
            return Response(home_assistant.start_docker(), mimetype='text/plain')

        elif action == "stop":
            return Response(home_assistant.stop_docker(), mimetype='text/plain')

        elif action == "restart":
            return Response(home_assistant.restart_docker(), mimetype='text/plain')

        elif action == "update":
            return Response(home_assistant.update_docker(), mimetype='text/plain')

        elif action == "backup":
            return Response(home_assistant.backup(), mimetype='text/plain')

    if project == "homebridge":
        if branch is None:
            homebridge = HomebridgeDeployment()
        else:
            homebridge = HomebridgeDeployment(branch)

        if action == "deploy":
            return Response(homebridge.deploy(), mimetype='text/plain')

        elif action == "start":
            return Response(homebridge.start_docker(), mimetype='text/plain')

        elif action == "stop":
            return Response(homebridge.stop_docker(), mimetype='text/plain')

        elif action == "restart":
            return Response(homebridge.restart_docker(), mimetype='text/plain')

        elif action == "update":
            return Response(homebridge.update_docker(), mimetype='text/plain')

        elif action == "backup":
            return Response(homebridge.backup(), mimetype='text/plain')

    if project == "deployment-hub-ui":
        if branch is None:
            deployment_hub_ui = DeploymentHubUIDeployment()
        else:
            deployment_hub_ui = DeploymentHubUIDeployment(branch)

        if action == "deploy":
            return Response(deployment_hub_ui.deploy(None, "/(Dockerfile|docker-compose.yml|.git|.env|.dockerignore)/g"),
                            mimetype='text/plain')

        elif action == "start":
            return Response(deployment_hub_ui.start_docker(), mimetype='text/plain')

        elif action == "stop":
            return Response(deployment_hub_ui.stop_docker(), mimetype='text/plain')

        elif action == "restart":
            return Response(deployment_hub_ui.restart_docker(), mimetype='text/plain')

        elif action == "update":
            return Response(deployment_hub_ui.update_docker(), mimetype='text/plain')

        elif action == "backup":
            return Response(deployment_hub_ui.backup(), mimetype='text/plain')

    if project == "deployment-hub":
        if branch is None:
            deployment_hub = DeploymentHubDeployment()
        else:
            deployment_hub = DeploymentHubDeployment(branch)

        if action == "deploy":
            return Response(deployment_hub.update_docker(), mimetype='text/plain')

        elif action == "start":
            return Response(deployment_hub.start_docker(), mimetype='text/plain')

        elif action == "stop":
            return Response(deployment_hub.stop_docker(), mimetype='text/plain')

        elif action == "restart":
            return Response(deployment_hub.restart_docker(), mimetype='text/plain')

        elif action == "backup":
            return Response(deployment_hub.backup(), mimetype='text/plain')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
