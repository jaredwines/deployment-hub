FROM ubuntu

#Update and install required libraries.
RUN apt-get update && apt-get install -y openssh-client python3-pip python3

#Configure ssh.
RUN useradd -m user
RUN mkdir -p /home/user/.ssh
RUN chown -R user:user /home/user/.ssh
RUN echo "Host *.trabe.io\n\tStrictHostKeyChecking no\n" >> /home/user/.ssh/config
RUN /bin/bash
USER user

WORKDIR /usr/src/deployment-hub
COPY . /usr/src/deployment-hub

RUN pip3 install --no-cache-dir -r /usr/src/deployment-hub/requirements.txt 

EXPOSE 5000

# run the application
CMD ["python3", "/usr/src/deployment-hub/src/deployment_hub.py"]