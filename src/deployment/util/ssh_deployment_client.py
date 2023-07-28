from flask import current_app
from paramiko import SSHConfig, SSHClient, RSAKey, AutoAddPolicy


class SshDeploymentClient:

    def __init__(self, host):
        self._host = host
        self.__ssh_client = self.__create_ssh_client()

    def __del__(self):
        self.__ssh_client.close()

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, host):
        self._host = host

    def __create_ssh_client(self):
        ssh_client = SSHClient()
        ssh_config = SSHConfig()
        ssh_config.parse(open("/root/.ssh/config"))
        ssh_config_properties = ssh_config.lookup(self.host)

        identity_file = ssh_config_properties['identityfile'][0]
        host_name = ssh_config_properties['hostname']
        user_name = ssh_config_properties['user']

        key = RSAKey.from_private_key_file(identity_file)

        ssh_client.set_missing_host_key_policy(AutoAddPolicy())
        ssh_client.connect(hostname=host_name, username=user_name, pkey=key)

        return ssh_client

    def exec_command(self, command):
        output = ""

        if isinstance(command, list):
            for x in command:
                current_app.logger.info(x)
                stdin, stdout, stderr = self.__ssh_client.exec_command(x)
                stdout.channel.set_combine_stderr(True)
                output = stdout.readlines()
                # while int(stdout.channel.recv_exit_status()) != 0: time.sleep(1)

                # for line in output:
                #     output = output + line
                current_app.logger.info(output)

        elif isinstance(command, str):
            current_app.logger.info(command)
            stdin, stdout, stderr = self.__ssh_client.exec_command(command)
            stdout.channel.set_combine_stderr(True)
            output = stdout.readlines()
            # while int(stdout.channel.recv_exit_status()) != 0: time.sleep(1)

            # for line in output:
            #     output = output + line
            current_app.logger.info(output)

        return output

    def exec_command_check(self, command):
        stdout = self.exec_command(
            "if [[ $(" + command + ") ]]; then echo 'True'; else echo 'False'; fi")
        current_app.logger.info(stdout.rstrip() + "check test")
        command_check = eval(stdout.rstrip())

        current_app.logger.info(command_check + "check")

        return command_check
