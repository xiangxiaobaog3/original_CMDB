# -*- coding:utf-8 -*-

from src.plugins import PluginsManager
from src.engine.base import BaseHandler

class AgentHandler(BaseHandler):

    def cmd(self, command, hostname=None):
        import subprocess
        ret = subprocess.getoutput(command)
        return ret

    def handler(self):
        """
        :return:
        """
        from src.plugins.disk import get_disk
        print('agent')

        ret = PluginsManager()
        print(ret)