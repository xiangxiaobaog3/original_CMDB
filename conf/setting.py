# -*- coding:utf-8 -*-

USER = 'xiangqian'

PWD = 123

ENGINE = 'ssh' # agent/ssh/salt

SSH_USER = 'root'
SSH_PORT = 2222
SSH_PWD = '123'

PLUGINS_DICT = {
    'basic': 'src.plugins.basic.Basic',
    'cpu': 'src.plugins.cpu.Cpu',
    'disk': 'src.plugins.disk.Disk',
    # 'memory': 'src.plugins.memory.Memory',
    'nic': 'src.plugins.nic.Nic',
}