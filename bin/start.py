# -*- coding:utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.plugins import PluginsManager

if __name__ == '__main__':

    res = PluginsManager().execute()
    print(res)
