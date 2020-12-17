FROM ubuntu

RUN apt update
RUN apt install -y git python3-pip python

WORKDIR /usr/src/
COPY . /usr/src/

RUN ls /usr/src/

RUN pip3 install --no-cache-dir -r /usr/src/deployment-hub/requirements.txt 

# tell the port number the container should expose
EXPOSE 5000

# run the application
CMD ["python", "/usr/src/deployment-hub/src/deployment.py"]