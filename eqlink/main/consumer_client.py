"""
用于客户端Consumer到注册中心的连接器
"""
import json
import socket
from time import sleep as time_sleep
from eqlink.components.remote_server import remote_server
from eqlink.components.code_msg import sys_error
import traceback

'''失效服务列表'''
fail_server_list = []


class LinkClient:
    def __init__(self, server_conf, client_conf):
        """
        初始化
        :param server_conf: 注册中心配置
        :param client_conf: Consumer客户端配置
        """
        self.server_conf = server_conf
        self.client_conf = client_conf

    def client_int(self, data_to_server):
        """
        consumer获取注册中心服务列表的线程对象
        :param data_to_server: 发送到注册中心的数据
        :return: None
        """
        try:  # 创建socket套接字
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as e:
            print("[eqlink] Error creating socket: %s" + str(e))
            print(traceback.format_exc())
            return sys_error('9001')

        try:  # 绑定ip和端口
            client.connect((self.server_conf['IP'], self.server_conf['PORT']))
            '''
            client.setblocking(flag):
            如果flag为0，则将套接字设为非阻塞模式，否则将套接字设为阻塞模式（默认值）
            非阻塞模式下，如果调用recv()没有发现任何数据，或send()调用无法立即发送数据，那么将引起socket.error异常
            '''
            print(f"[eqlink] connect link server success on {self.server_conf['IP']}:{self.server_conf['PORT']}")
        except socket.error as e:
            print('[eqlink] connected to link center error: %s' + str(e))
            print(traceback.format_exc())
            return sys_error('9002')

        while True:  # 与注册中心保持连接，定时获取服务列表
            fail_server_flag = False if len(data_to_server['invalid_service']) == 0 else True  # 判断是否存在调用失效的服务
            try:
                data_json = json.dumps(data_to_server)  # json转str
                client.sendall(bytes(data_json, encoding="utf8"))  # 向注册中心发送信息，获取可用服务列表
                data = client.recv(self.server_conf['BUF_SIZE'])  # 设置接收注册中心返回信息大小
                remote_server.__set__(json.loads(data))  # 服务列表写入本地共享的内存中
                if fail_server_flag:  # 移除本地存储的，用于与注册中心交互的的失效服务列表
                    data_to_server['fail_server'] = []
            except socket.error as e:
                print('[eqlink] consumer get provider list send failed: ', e)
                print(traceback.format_exc())
                break
            time_sleep(self.client_conf['alive'])  # 间隔一段时间，进行一次心跳检擦，心跳数据设置
        return sys_error('9003')
