"""
服务消费消费者连接注册中心
"""

import socket
from eqlink.main.provider_register import LinkRegister

if __name__ == '__main__':
    ip = socket.gethostbyname(socket.gethostname())
    SERVER_CONF = {
        # 远程服务器地址
        'IP': '11.11.0.127',
        # 远程服务器端口
        'PORT': 7878,
        # 消息读取长度
        'BUF_SIZE': 1024
    }
    '''请求信息'''
    SEND_DATA = {
        'type': 'provider register',
        'remote': {'ip': ip, 'port': '889'},
        'service_name': 'order_service',
        'func': ['add_order', 'order_list']
    }
    LinkRegister(SERVER_CONF).register_int(SEND_DATA)
