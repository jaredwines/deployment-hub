FROM ubuntu

RUN apt-get update
RUN apt-get install -y git python3-pip python3

WORKDIR /usr/src/deployment-hub
COPY . /usr/src/deployment-hub

RUN python3 --version

RUN pip3 install --no-cache-dir -r /usr/src/deployment-hub/requirements.txt 

# tell the port number the container should expose
EXPOSE 5000

# run the application
CMD ["python3", "/usr/src/deployment-hub/src/deployment_hub.py"]