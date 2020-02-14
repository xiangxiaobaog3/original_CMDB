# -*- coding:utf-8 -*-

class Basic(object):

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
        key_map = {
            "Manufacturer": 'manufacturer',
            'Product Name': 'product_name',
            'Serial Number': 'sn'
        }

        response = {}
        res = res.split('\n')
        for info in res:
            if info:
                v = info.strip().split(':')
                if len(v) == 2:
                    if v[0] in key_map:
                        response[key_map[v[0]]] = v[1]

        return (response)