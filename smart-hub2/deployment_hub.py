from flask import Flask
from home_assistant_deployment import HomeAssistantDeployment
from jaredwines_com_deployment import JaredWinesComDeployment
import sys

app = Flask(__name__)

@app.route('/deploy-jaredwinescom/host/<host>/gitRepo/<gitRepo>/branch/<branch>/maintence-mode/<maintence>', methods=['POST', 'GET'])
def deploy_jaredwinescom(host, gitRepo, branch, maintence):
    deploy_jaredwines_com=JaredWinesComDeployment(host, gitRepo, branch)
    return deploy_jaredwines_com.deploy()

@app.route('/deploy-home-assistant/host/<host>/gitRepo/<gitRepo>/branch/<branch>', methods=['POST', 'GET'])
def deploy_home_assistant(host=None, gitRepo=None, branch=None):
    deploy_jaredwines_com=HomeAssistantDeployment(host, gitRepo, branch)
    return deploy_jaredwines_com.deploy()

@app.route('/test', methods=['GET'])
def test():
    return "test"

if __name__ == '__main__':
    app.run()
