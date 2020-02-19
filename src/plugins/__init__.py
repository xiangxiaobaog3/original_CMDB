# -*- coding:utf-8 -*-

import os
import sys
import importlib

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.config.settings import settings
from lib.util.import_str import get_class


# class PluginsManager(object):
#
#     def __init__(self, hostname=None):
#         self.plugins_dict = settings.PLUGINS_DICT
#
#     # 管理配置文件种采集的插件
#     def execute(self):
#
#         response = {}
#         # 首先获取配置文件中 PLUGINS_DICT 循环获取
#         for name, path in self.plugins_dict.items():
#             cls = get_class(path)
#             obj = cls()
#             # 一个函数当成一个参数方式传给每个插件的process函数
#             res = obj.process()
#             response[name] = res
#             # res = cls().process(self._cmd_run)
#         return response

def get_server_info(handler, hostname=None):
    # 根据配置获取相应的硬件信息
    response = {}
    # 首先获取配置文件中 PLUGINS_DICT 循环获取
    for name, path in settings.PLUGINS_DICT.items():
        cls = get_class(path)
        obj = cls()
        # 一个函数当成一个参数方式传给每个插件的process函数
        res = obj.process(handler, hostname)
        response[name] = res
        # res = cls().process(self._cmd_run)
    return response



    # def _cmd_run(self, cmd):
    #     if self.mode == 'agent':
    #         return self.__cmd_agent(cmd)
    #     elif self.mode == 'ssh':
    #         return self.__cmd_ssh(cmd)
    #     elif self.mode == 'salt':
    #         return self.__cmd_salt(cmd)
    #     else:
    #         raise Exception('当前支持的模式只有：agent/ssh/salt模式')

