# -*- coding:utf-8 -*-
from lib.config.settings import settings
from src.engine.base import BaseHandler
import salt
from src.plugins import PluginsManager

class SaltHandler(BaseHandler):

    def cmd(self, command, hostname):
        import salt.client
        local = salt.client.LocalClient()
        res = local.cmd(hostname, 'cmd.run', [command])
        return res[hostname]

    def handler(self):
        """
        :return:
        """
        print('salt')