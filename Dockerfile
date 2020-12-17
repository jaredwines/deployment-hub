FROM ubuntu

RUN apt-get update
RUN apt-get install -y git python3-pip python3

#RUN apt-get update && apt-get install -y git python3-pip python3 openssh-client docker-compose
RUN apt-get update && apt-get install -y openssh-client


RUN useradd -m user
RUN mkdir -p /home/user/.ssh
RUN chown -R user:user /home/user/.ssh
RUN echo "Host *.trabe.io\n\tStrictHostKeyChecking no\n" >> /home/user/.ssh/config
RUN /bin/bash
USER user

WORKDIR /usr/src/deployment-hub
COPY . /usr/src/deployment-hub

#RUN pip3 install --no-cache-dir -r /usr/src/deployment-hub/requirements.txt 

# tell the port number the container should expose
EXPOSE 5000

# run the application

#CMD ["python3", "/usr/src/deployment-hub/src/deployment_hub.py"]
CMD ["/bin/bash"]