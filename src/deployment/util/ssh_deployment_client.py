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
        #current_app.logger.info(command)
        stdin, stdout, stderr = self.__ssh_client.exec_command(command)
        stdout.channel.set_combine_stderr(True)
        output_list = stdout.readlines()
        # current_app.logger.info(stdout)
        # current_app.logger.info(output_list)

        for output in output_list:
            if output:
                current_app.logger.info(output)

        return output_list

    def exec_command_list(self, command_list):
        output_list = []

        for command in command_list:
            output_list.extend(self.exec_command(command))

        return output_list

    def exec_command_check(self, command):
        output_list = self.exec_command(
            "if [[ $(" + command + ") ]]; then echo 'True'; else echo 'False'; fi")
        current_app.logger.info(output_list[0] + "check test")
        command_check = eval(output_list[0].rstrip())

        current_app.logger.info("testcommand_check")
        current_app.logger.info(command_check)

        return command_check

    def exec_command_is_dir(self, target_dir):
        output_list = self.exec_command(
            "if [[ -d " + target_dir + " ]]; then echo 'True'; else echo 'False'; fi")
        command_check = eval(output_list[0].rstrip())

        return command_check
