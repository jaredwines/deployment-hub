from flask import Flask, Response

from src.deployment.deployment_hub_deployment import DeploymentHubDeployment
from src.deployment.home_assistant_deployment import HomeAssistantDeployment
from src.deployment.jared_wines_com_deployment import JaredWinesComDeployment

app = Flask(__name__)


@app.route('/<project>/', methods=['POST', 'GET'])
@app.route('/<project>/<action>/', methods=['POST', 'GET'])
@app.route('/<project>/<action>/<branch>', methods=['POST', 'GET'])
def deploy(project=None, branch=None, action=None):
    if project == "jaredwines-portfolio":
        if branch is None:
            jared_wines_com = JaredWinesComDeployment()
        else:
            jared_wines_com = JaredWinesComDeployment(branch)

        if action == "deploy":
            return Response(jared_wines_com.deploy(), mimetype='text/plain')

        if action == "maintenance-mode":
            jared_wines_com.maintenance_flag = "True"
            return Response(jared_wines_com.deploy(), mimetype='text/plain')

        elif action is None:
            return Response(jared_wines_com.deploy(), mimetype='text/plain')

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

        elif action is None:
            return Response(home_assistant.deploy(), mimetype='text/plain')

    if project == "deployment-hub-server":
        if branch is None:
            deployment_hub = DeploymentHubDeployment()
        else:
            deployment_hub = DeploymentHubDeployment(branch)

        if action == "deploy":
            return Response(deployment_hub.update(), mimetype='text/plain')
        elif action is None:
            return Response(deployment_hub.update(), mimetype='text/plain')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
