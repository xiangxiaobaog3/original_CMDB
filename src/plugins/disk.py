# -*- coding:utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.plugins.Base import Base

class Disk(Base):

    def process(self):
        self.exec_command('df -h')