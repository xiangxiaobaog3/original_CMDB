# -*- coding:utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.config.settings import settings
from src.engine import ssh
from src.engine import agent
from src.engine import salt


def run():
    """

    程序入口

    :return:
    """

    if settings.ENGINE == 'agent':
        obj = agent.AgentHandler()
        obj.handler()
    elif settings.ENGINE == 'ssh':
        obj = ssh.SSHHandler()
        obj.handler()
    elif settings.ENGINE == 'salt':
        obj = salt.SaltHandler()
        obj.handler()
    else:
        raise Exception('当前支持的模式只有：agent/ssh/salt模式')

run()