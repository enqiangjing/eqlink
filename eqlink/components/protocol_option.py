"""
公共工具，协议分析
"""
from eqlink.components.link_list import LinkList
import json
import traceback

''' 全局共享：注册中心连接列表 '''
link_list = LinkList()


def protocol_analysis(protocol, storage_path):
    """
    对协议类型进行分析和处理
    :param storage_path: 本地持久化文件路径
    :param protocol: JSON协议数据
    :return: None
    """
    if protocol['type'] == 'provider register':
        link_list.add_provider(protocol)  # Provider注册
        server_backup(storage_path)  # Provider服务列表本地持久化存储
        return {'code': '1000', 'message': '服务注册执行完成!'}
    elif protocol['type'] == 'get service':  # Consumer查询Provider服务列表
        fail_server = protocol['fail_server']
        for item in link_list.provider_list:  # 遍历已注册的服务列表
            print('[eqlink] 失败服务:', protocol['fail_server'], '在线服务:', item, link_list.provider_list[item]['remote'])
            remote_list = link_list.provider_list[item]['remote']
            for i in remote_list:  # 循环读取，移除失败的调用服务的IP和PORT
                for j in fail_server:
                    if i['ip'] == j['IP'] and i['port'] == j['PORT']:
                        link_list.provider_list[item]['remote'].remove(i)
        server_backup(storage_path, False)
        return link_list.provider_list


def server_backup(storage_path, backup=True):
    """
    Provider list 持久化
    :param storage_path: 本地文件存储路径
    :param backup: 是否更新备份缓存
    :return: None
    """
    try:
        f = open(storage_path, "w", encoding="utf-8")
        f.write(json.dumps(link_list.provider_list))
        if backup:
            link_list.provider_list_backup = link_list.provider_list.copy()
    except Exception as e:
        print(traceback.format_exc())
        print('[eqlink] 文件存储失败', e)
