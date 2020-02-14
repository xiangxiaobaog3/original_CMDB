import importlib

res = importlib.import_module('s3')

cls = getattr(res, 'Person')

cls().getinfo()