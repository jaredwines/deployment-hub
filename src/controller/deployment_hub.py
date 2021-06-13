from flask import Flask, Response

from src.deployment.home_assistant_deployment import HomeAssistantDeployment
from src.deployment.jared_wines_com_deployment import JaredWinesComDeployment
from src.deployment.deployment_hub_deployment import DeploymentHubDeployment


app = Flask(__name__)


@app.route('/deploy-jaredwinescom/', methods=['POST', 'GET'])
@app.route('/deploy-jaredwinescom/<branch>/', methods=['POST', 'GET'])
@app.route('/deploy-jaredwinescom/<branch>/<maintenance_flag>', methods=['POST', 'GET'])
def jaredwines_com_deploy(branch=None, maintenance_flag=None):
    jared_wines_com = JaredWinesComDeployment(branch)

    if maintenance_flag is not None:
        jared_wines_com.maintenance_flag = maintenance_flag

    return Response(jared_wines_com.deploy(), mimetype='text/plain')


@app.route('/deploy-home-assistant/', methods=['POST', 'GET'])
@app.route('/deploy-home-assistant/<branch>', methods=['POST', 'GET'])
@app.route('/deploy-home-assistant/<branch>/<action>', methods=['POST', 'GET'])
def home_assistant_deploy(branch=None, action=None):
    home_assistant = HomeAssistantDeployment(branch)

    if action is None:
        return Response(home_assistant.deploy(), mimetype='text/plain')

    elif action == "start":
        return Response(home_assistant.start_docker(), mimetype='text/plain')

    elif action == "stop":
        return Response(home_assistant.stop_docker(), mimetype='text/plain')

    elif action == "restart":
        return Response(home_assistant.restart_docker(), mimetype='text/plain')

    elif action == "update":
        return Response(home_assistant.update_docker(), mimetype='text/plain')


@app.route('/deploy-deployment-hub/', methods=['POST', 'GET'])
@app.route('/deploy-deployment-hub/<branch>/', methods=['POST', 'GET'])
def deployment_hub_deploy(branch=None):
    deployment_hub = DeploymentHubDeployment(branch)

    return Response(deployment_hub.update(), mimetype='text/plain')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
