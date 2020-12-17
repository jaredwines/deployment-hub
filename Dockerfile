FROM ubuntu

ARG branch="master"

RUN apt update
RUN apt install -y git python3-pip python

RUN mkdir /usr/src/deployment-hub/
WORKDIR /usr/src/deployment-hub/

RUN git clone -b ${branch} git@github.com:jaredwines/deployment-hub.git /usr/src/deployment-hub/

RUN pip install --no-cache-dir -r /usr/src/deployment-hub/requirements.txt 

# tell the port number the container should expose
EXPOSE 5000

# run the application
CMD ["python", "/usr/src/deployment-hub/src/deployment.py"]