# -*- coding:utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# from src.plugins.Base import Base
#
class Disk():

    def process(self, handler, hostname=None):
        ret = handler.cmd('df -h', hostname)
        return ret

# def get_disk(handler, hostname=None):
#     ret = handler.cmd('df -h', hostname)
#     print(ret)