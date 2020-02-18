# -*- coding:utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.config.settings import settings
import importlib


def run():
    """
    程序入口

    开放封闭原则
    开放：配置
    封闭：源码

    :return:
    """

    # if settings.ENGINE == 'agent':
    #     obj = agent.AgentHandler()
    #     obj.handler()
    # elif settings.ENGINE == 'ssh':
    #     obj = ssh.SSHHandler()
    #     obj.handler()
    # elif settings.ENGINE == 'salt':
    #     obj = salt.SaltHandler()
    #     obj.handler()
    # else:
    #     raise Exception('当前支持的模式只有：agent/ssh/salt模式')

    engine_path = settings.ENGINE_DICT.get(settings.ENGINE)
    module_name, class_name = engine_path.rsplit('.', 1)
    # 将一个包以字符串的形式导入 获取模块
    module = importlib.import_module(module_name)
    # 反射获取到类
    cls = getattr(module, class_name)
    # 实例化对象 执行handler()
    obj = cls()
    obj.handler()
run()