# -*- coding:utf-8 -*-

import os
import sys
import importlib

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.config.settings import settings


class PluginsManager(object):

    def __init__(self):
        self.plugins_dict = settings.PLUGINS_DICT
        self.mode = settings.MODE

    # 管理配置文件种采集的插件
    def execute(self):

        response = {}
        # 首先获取配置文件中 PLUGINS_DICT 循环获取
        for k, v in self.plugins_dict.items():

            module_name, class_name = v.rsplit('.', 1)

            # 将一个包以字符串的形式导入
            module_path = importlib.import_module(module_name)

            # 将值的类导入并实例化，执行process方法
            cls = getattr(module_path, class_name)
            res = cls().process(self._cmd_run)
            response[k] = res

            # 一个函数当成一个参数方式传给每个插件的process函数
            # res = cls().process(self._cmd_run)


        return response


    def _cmd_run(self, cmd):
        if self.mode == 'agent':
            return self.__cmd_agent(cmd)
        elif self.mode == 'ssh':
            return self.__cmd_ssh(cmd)
        elif self.mode == 'salt':
            return self.__cmd_salt(cmd)
        else:
            raise Exception('当前支持的模式只有：agent/ssh/salt模式')

    def __cmd_agent(self, cmd):
        import subprocess

        res = subprocess.getoutput(cmd)
        return res


    def __cmd_ssh(self, cmd):
        import paramiko

        # 创建SSH对象
        ssh = paramiko.SSHClient()
        # 允许连接不在know_hosts文件中的主机
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接服务器
        ssh.connect(hostname='s1.talkren.cn', port=2222, username='root', password='***')
        # 执行命令
        stdin, stdout, stderr = ssh.exec_command('df')
        # 获取命令结果
        result = stdout.read()
        # 关闭连接
        ssh.close()
        return result


    def __cmd_salt(self, cmd):
        import subprocess
        res = subprocess.getoutput("salt 's1.talkren.cn' cmd.run 'ifconfig'")
        return res