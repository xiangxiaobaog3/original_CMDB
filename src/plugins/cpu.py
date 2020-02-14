# -*- coding:utf-8 -*-

class Cpu(object):

    def process(self, command_func, debug):

        if debug:
            res = command_func('hostname')
        else:
            res = command_func('hostname')

        # return ('this is Cpu')

        self.parse(res)

    def parse(self, res):
        pass
        # 具体分析的代码