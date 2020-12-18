from flask import Flask
from jared_wines_com_deployment import JaredWinesComDeployment
from home_assistant_deployment import HomeAssistantDeployment

app = Flask(__name__)


@app.route('/deploy-jaredwinescom/', methods=['POST', 'GET'])
@app.route('/deploy-jaredwinescom/<branch>/', methods=['POST', 'GET'])
@app.route('/deploy-jaredwinescom/<branch>/<maintenance_flag>', methods=['POST', 'GET'])
def jaredwines_com_deploy(branch = None, maintenance_flag = None) :
    jared_wines_com = JaredWinesComDeployment()

    if not branch == None:
        jared_wines_com.branch = branch

    if not maintenance_flag == None:
        jared_wines_com.maintenance_flag = maintenance_flag

    home_assistant.connect_ssh_client()
    jared_wines_com.deploy()
    jared_wines_com.close_ssh_client()
    
    return "Completed jaredwines.com Deployment."

@app.route('/deploy-home-assistant/', methods=['POST', 'GET'])
@app.route('/deploy-home-assistant/<branch>', methods=['POST', 'GET'])
def home_assistant_deploy(branch = None):
    home_assistant = HomeAssistantDeployment()

    if not branch == None :
        home_assistant.branch = branch

    home_assistant.connect_ssh_client()
    home_assistant.deploy()
    home_assistant.close_ssh_client()

    return "Completed Home Assistant Deployment."

@app.route('/deploy-home-assistant/start', methods=['POST', 'GET'])
def deploy_home_assistant_start():
    home_assistant = HomeAssistantDeployment()

    home_assistant.connect_ssh_client()
    home_assistant.start()
    home_assistant.close_ssh_client()

    return "Completed starting Home Assistant."

@app.route('/deploy-home-assistant/restart', methods=['POST', 'GET'])
def deploy_home_assistant_restart():
    home_assistant = HomeAssistantDeployment()

    home_assistant.connect_ssh_client()
    home_assistant.restart()
    home_assistant.close_ssh_client()

    return "Completed restarting Home Assistant."

@app.route('/deploy-home-assistant/stop', methods=['POST', 'GET'])
def deploy_home_assistant_stop():
    home_assistant = HomeAssistantDeployment()

    home_assistant.connect_ssh_client()
    home_assistant.stop()
    home_assistant.close_ssh_client()

    return "Completed stoping Home Assistant."

@app.route('/deploy-home-assistant/update', methods=['POST', 'GET'])
def deploy_home_assistant_update():
    home_assistant = HomeAssistantDeployment()
    
    home_assistant.connect_ssh_client()
    home_assistant.update()
    home_assistant.close_ssh_client()

    return "Completed updating Home Assistant."

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)