# -*- coding:utf-8 -*-
import os
import sys
import importlib

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.config.settings import settings

class PluginsManager(object):

    def __init__(self):
        self.plugins_dict = settings.PLUGINS_DICT

    ### 管理配置文件种采集的插件
    def execute(self):

        response = {}
        ### 首先获取配置文件中 PLUGINS_DICT 循环获取
        for k, v in self.plugins_dict.items():

            module_name, class_name = v.rsplit('.', 1)

            ### 将一个包以字符串的形式导入
            module_path = importlib.import_module(module_name)

            ### 将植的类导入并实例化，执行process方法
            cls = getattr(module_path, class_name)
            res = cls().process()
            response[k] = res

        return response
