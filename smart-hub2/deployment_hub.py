from flask import Flask
from jaredwines_com_deployment import JaredWinesComDeployment
from home_assistant_deployment import HomeAssistantDeployment

app = Flask(__name__)


@app.route('/deploy-jaredwinescom/', methods=['POST', 'GET'])
@app.route('/deploy-jaredwinescom/<branch>/', methods=['POST', 'GET'])
@app.route('/deploy-jaredwinescom/<branch>/<maintenance_flag>', methods=['POST', 'GET'])
def deploy_jaredwinescom(branch=None, maintenance_flag=None) :
    if branch == None and maintenance_flag == None :
        deploy_jaredwines_com=JaredWinesComDeployment()
    elif maintenance_flag == None :
        deploy_jaredwines_com=JaredWinesComDeployment(branch)
    elif branch == None :
        deploy_jaredwines_com=JaredWinesComDeployment(maintenance_flag)
    else :
        deploy_jaredwines_com=JaredWinesComDeployment(branch, maintenance_flag)

    return deploy_jaredwines_com.deploy()

@app.route('/deploy-home-assistant/', methods=['POST', 'GET'])
@app.route('/deploy-home-assistant/<branch>', methods=['POST', 'GET'])
def deploy_home_assistant(branch=None):
    if branch == None :
        deploy_jaredwines_com=HomeAssistantDeployment()
    else :
        deploy_jaredwines_com=HomeAssistantDeployment(branch)

    return deploy_jaredwines_com.deploy()

if __name__ == '__main__':
    app.run()
