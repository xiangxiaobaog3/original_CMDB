import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.config.settings import settings

# if __name__ == '__main':
#     settings1 = settings.settings
#     print(settings1)
print(settings.USER)

