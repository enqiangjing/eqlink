"""
Consumer 连接注册中心
"""

import socket
from eqlink.main.clent import LinkClient

if __name__ == '__main__':
    ip = socket.gethostbyname(socket.gethostname())
    service_conf = {
        # 远程服务器地址
        'IP': '11.11.0.127',
        # 远程服务器端口
        'PORT': 7878,
        # 消息读取长度
        'BUF_SIZE': 1024
    }
    client_conf = {
        # 心跳检测时间间隔，单位S
        'alive': 20
    }
    data_to_server = {
        'type': 'get provider',
        'ip': ip
    }
    LinkClient(service_conf, client_conf).client_int(data_to_server)
