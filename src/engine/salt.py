
from src.engine.base import BaseHandler

class SaltHandler(BaseHandler):

    def handler(self):
        """
        import subprocess
        res = subprocess.getoutput("salt '%s' cmd.run '%s'" % (self.hostname, cmd))
        return res
        :return:
        """
        print('salt')