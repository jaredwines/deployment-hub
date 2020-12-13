from flask import Flask
from home_assistant_deployment import HomeAssistantDeployment
from jaredwines_com_deployment import JaredWinesComDeployment
import sys

app = Flask(__name__)

@app.route('/deploy-jaredwinescom/<branch>/<maintenance_flag>', methods=['POST', 'GET'])
def deploy_jaredwinescom(branch, maintenance_flag=None):
    deploy_jaredwines_com=JaredWinesComDeployment(branch)
    return deploy_jaredwines_com.deploy()

@app.route('/deploy-home-assistant/<branch>', methods=['POST', 'GET'])
def deploy_home_assistant(branch=None):
    deploy_jaredwines_com=HomeAssistantDeployment(branch)
    return deploy_jaredwines_com.deploy()

@app.route('/test', methods=['GET'])
def test():
    return "test"

if __name__ == '__main__':
    app.run()
