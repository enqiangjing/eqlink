"""
注册中心服务启动
"""
import socket
from eqlink.main.registry_server import LinkServer

if __name__ == '__main__':
    '''本机IP'''
    HOST = socket.gethostname()
    '''配置信息'''
    SERVER_CONF = {
        'HOST': HOST,
        'PORT': 7878,
        'BUF_SIZE': 1024,
        'BACKLOG': 5
    }
    LinkServer(SERVER_CONF, 'server_list.json').server_init()
