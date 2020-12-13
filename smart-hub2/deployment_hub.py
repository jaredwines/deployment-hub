from flask import Flask
from home_assistant_deployment import HomeAssistantDeployment
from jaredwines_com_deployment import JaredWinesComDeployment
import sys

app = Flask(__name__)

@app.route('/deploy-jaredwinescom/host=<host>/gitRepo=<gitRepo>/branch=<branch>/maintence-mode=<maintence>')
def deploy_jaredwinescom(host, gitRepo, branch, maintence):
    deploy_jaredwines_com=JaredWinesComDeployment(host, gitRepo, branch)
    return deploy_jaredwines_com.deploy()

@app.route('/deploy-home-assistant/host=<host>/gitRepo=<gitRepo>/branch=<branch>/')
def deploy_home_assistant(host, gitRepo, branch):
    deploy_jaredwines_com=HomeAssistantDeployment(host, gitRepo, branch)
    return deploy_jaredwines_com.deploy()

if __name__ == '__main__':
    app.run()
