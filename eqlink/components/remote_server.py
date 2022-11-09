"""
远程服务：用于Consumer客户端本地读取Provider列表
1.
"""


class RemoteServer:
    def __init__(self):
        self.remote_server = {}

    def __get__(self):
        return self.remote_server

    def __set__(self, data):
        self.remote_server = data


''' 用于共享的远程服务列表对象 '''
remote_server = RemoteServer()
