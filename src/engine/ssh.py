# -*- coding:utf-8 -*-
from lib.config.settings import settings
from src.engine.base import BaseHandler
from src.plugins import get_server_info

class SSHHandler(BaseHandler):

    """
    同样的执行命令，但执行方式不一样
    """

    def cmd(self, command, hostname):
        import paramiko
        # 创建SSH对象
        ssh = paramiko.SSHClient()
        # 允许连接不在know_hosts文件中的主机
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接服务器
        ssh.connect(hostname=hostname, port=settings.SSH_PORT, username=settings.SSH_USER, password=settings.SSH_PWD)
        # 执行命令
        stdin, stdout, stderr = ssh.exec_command(command)
        # 获取命令结果
        result = stdout.read()
        # 关闭连接
        ssh.close()
        return result


    def handler(self):
        """

        :return:
        """
        # from src.plugins.disk import get_disk
        # get_disk(self, '108.160.135.123')

# cc = SSHHandler().cmd('df -h')
# print(cc)

        ret = get_server_info(self, '108.160.135.123')
        print(ret)