"""
yaml配置文件读取工具
"""
import json
import traceback


def json_file_read(file_path):
    """
    读取json文件
    :param file_path: 文件路径
    :return: 文件内容（文件内容需要为json格式）
    """
    try:
        with open(file_path, encoding='utf-8') as json_file:
            fie_data = json.load(json_file)
            return fie_data
    except Exception as e:
        print('[Error] 配置文件读取失败：', str(e))
        print(traceback.format_exc())
        return {}


class ReadConf:
    def __init__(self, file_path):
        """
        对象初始化初始化
        :param file_path: 配置文件路径
        """
        self.conf_path = file_path
        self.configuration = {}

    def __read__(self, item):
        """
        配置项读取
        :param item: 配置项，如 a.b.c
        :return: 配置值
        """
        '''
        1.先判断 configuration 是否有内容，无内容则先加载配置文件。
        2.
        '''
        if bool(self.configuration) is False:
            self.configuration = json_file_read(self.conf_path)
        items = item.split('.')
        return self.__item_read__(items)

    def __file_load__(self):
        """
        配置文件加载
        :return: None
        """
        if bool(self.configuration) is False:
            self.configuration = json_file_read(self.conf_path)

    def __item_read__(self, items):
        """
        按层级读取配置项
        :param items: 配置层级，如 ['a', 'b', 'c']
        :return:
        """
        result = self.configuration
        for i in items:
            result = result[i]
        return result
