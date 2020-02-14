# -*- coding:utf-8 -*-

### 将公用的代码抽离出来，写成一个基类，后续，如果还有其他的插件，则需要继承基类
class Base(object):

    def exec_command(self, cmd):
        pass
