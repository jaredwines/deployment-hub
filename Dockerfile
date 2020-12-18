FROM ubuntu

#Update and install required libraries.
RUN apt-get update && apt-get install -y openssh-client python3-pip python3

#Configure ssh.
RUN mkdir -p /root/.ssh
RUN echo "Host *.trabe.io\n\tStrictHostKeyChecking no\n" >> /root/.ssh/config
RUN /bin/bash

WORKDIR /usr/src/deployment-hub
COPY . /usr/src/deployment-hub

RUN pip3 install --no-cache-dir -r /usr/src/deployment-hub/requirements.txt 

EXPOSE 5000

# run the application
CMD ["python3", "/usr/src/deployment-hub/src/deployment_hub.py"]

#To run docker image use the following commond. 
# $ docker run -d --name="deployment-hub" -p 5000:5000 -v ~/.ssh:/root/.ssh deployment-hub