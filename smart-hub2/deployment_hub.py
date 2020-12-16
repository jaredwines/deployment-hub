from flask import Flask
from jaredwines_com_deployment import JaredWinesComDeployment
from home_assistant_deployment import HomeAssistantDeployment

app = Flask(__name__)


@app.route('/deploy-jaredwinescom/', methods=['POST', 'GET'])
@app.route('/deploy-jaredwinescom/<branch>/', methods=['POST', 'GET'])
@app.route('/deploy-jaredwinescom/<branch>/<maintenance_flag>', methods=['POST', 'GET'])
def deploy_jaredwinescom(branch = None, maintenance_flag = None) :
    deploy_jaredwines_com = JaredWinesComDeployment()

    if not branch == None:
        deploy_jaredwines_com.branch = branch

    if not maintenance_flag == None:
        deploy_jaredwines_com.maintenance_flag = maintenance_flag

    deploy_jaredwines_com.deploy()
    
    return "completed"

@app.route('/deploy-home-assistant/', methods=['POST', 'GET'])
@app.route('/deploy-home-assistant/<branch>', methods=['POST', 'GET'])
def deploy_home_assistant(branch = None):
    deploy_jaredwines_com = HomeAssistantDeployment()

    if branch == None :
        deploy_jaredwines_com.branch = branch

    deploy_jaredwines_com.deploy()

    return "completed"

if __name__ == '__main__':
    app.run()
