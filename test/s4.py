# -*- coding:utf-8 -*-

### 测试将一个包以字符串的方式导入
import importlib

res = importlib.import_module('s3')

cls = getattr(res, 'Person')

cls().getinfo()