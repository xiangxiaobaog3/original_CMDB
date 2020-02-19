# -*- coding:utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.config.settings import settings
from lib.util.import_str import get_class


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

    cls = get_class(engine_path)
    # 实例化对象 执行handler()
    obj = cls()
    obj.handler()