# -*- coding:utf-8 -*-

import importlib

def get_class(path):
    module_name, class_name = path.rsplit('.', 1)
    # 将一个包以字符串的形式导入 获取模块
    module = importlib.import_module(module_name)
    # 反射获取到类
    return getattr(module, class_name)