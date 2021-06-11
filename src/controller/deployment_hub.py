from flask import Flask, Response

from src.deployment.home_assistant_deployment import HomeAssistantDeployment
from src.deployment.jared_wines_com_deployment import JaredWinesComDeployment

app = Flask(__name__)


@app.route('/deploy-jaredwinescom/', methods=['POST', 'GET'])
@app.route('/deploy-jaredwinescom/<branch>/', methods=['POST', 'GET'])
@app.route('/deploy-jaredwinescom/<branch>/<maintenance_flag>', methods=['POST', 'GET'])
def jaredwines_com_deploy(branch=None, maintenance_flag=None):
    jared_wines_com = JaredWinesComDeployment()

    if not branch == None:
        jared_wines_com.branch = branch

    if not maintenance_flag == None:
        jared_wines_com.maintenance_flag = maintenance_flag

    jared_wines_com.deploy()

    return Response(jared_wines_com.deploy(), mimetype='text/plain')


@app.route('/deploy-home-assistant/', methods=['POST', 'GET'])
@app.route('/deploy-home-assistant/<branch>', methods=['POST', 'GET'])
def home_assistant_deploy(branch=None):
    home_assistant = HomeAssistantDeployment()

    if not branch == None:
        home_assistant.branch = branch

    home_assistant.deploy()

    return Response(home_assistant.deploy(), mimetype='text/plain')


@app.route('/deploy-home-assistant/start', methods=['POST', 'GET'])
def deploy_home_assistant_start():
    home_assistant = HomeAssistantDeployment()
    home_assistant.start_docker()

    return Response(home_assistant.start_docker(), mimetype='text/plain')


@app.route('/deploy-home-assistant/restart', methods=['POST', 'GET'])
def deploy_home_assistant_restart():
    home_assistant = HomeAssistantDeployment()

    home_assistant.restart_docker()

    return Response(home_assistant.restart_docker(), mimetype='text/plain')


@app.route('/deploy-home-assistant/stop', methods=['POST', 'GET'])
def deploy_home_assistant_stop():
    home_assistant = HomeAssistantDeployment()

    home_assistant.stop_docker()

    return Response(home_assistant.stop_docker(), mimetype='text/plain')


@app.route('/deploy-home-assistant/update', methods=['POST', 'GET'])
def deploy_home_assistant_update():
    home_assistant = HomeAssistantDeployment()

    home_assistant.update_docker()

    return Response(home_assistant.update_docker(), mimetype='text/plain')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
