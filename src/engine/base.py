
# import abc

# class BaseHandler(metaclass=abc.ABCMeta):
#
#     @abc.abstractmethod
#     def handler(self):
#         """
#         抽象类方法和抛出异常 必须要设置handler方法
#         区别在于没有定义报错和没有使用才会报错
#         :return:
#         """
#         pass

class BaseHandler():

    def cmd(self, command, hostname):
        raise NotImplementedError('cmd() must be Implemented')

    def handler(self):
        raise NotImplementedError('handler() must be Implemented')