FROM ubuntu

RUN apt update
RUN apt install -y git python3-pip python

WORKDIR /usr/src/deployment-hub
COPY . /usr/src/deployment-hub

RUN ls /usr/src/deployment-hub

RUN pip3 install --no-cache-dir -r /usr/src/deployment-hub/requirements.txt 

# tell the port number the container should expose
EXPOSE 5000

# run the application
CMD ["python", "/usr/src/deployment-hub/src/deployment_hub.py"]