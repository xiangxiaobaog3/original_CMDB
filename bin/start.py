# -*- coding:utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.plugins import PluginsManager

if __name__ == '__main__':

    host_list = ['10.10.0.100', '10.10.0.101']

    for host in host_list:

        res = PluginsManager(host).execute()
        print(res)
