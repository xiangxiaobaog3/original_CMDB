import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from conf import setting
from lib.config import global_settings

class Settings():
    def __init__(self):


        for key in dir(global_settings):
            if key.isupper():
                v = getattr(global_settings, key)
                setattr(self, key, v)

        for key in dir(setting):
            if key.isupper():
                v = getattr(setting, key)
                setattr(self, key, v)

settings = Settings()