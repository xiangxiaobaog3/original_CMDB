# -*- coding:utf-8 -*-


from src.engine.base import BaseHandler
# from src.plugins import get_server_info

class AgentHandler(BaseHandler):

    def cmd(self, command, hostname=None):
        import subprocess
        ret = subprocess.getoutput(command)
        return ret

    def handler(self):
        """
        :return:
        from src.plugins.disk import get_disk
        """

        print('agent')