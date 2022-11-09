"""
扩展工具
"""


def not_contain_key(source_dict, target_key):
    """
    判断dict不包含元素
    :param source_dict: 字典
    :param target_key: key
    :return: source_dict 不包含 target_key, 返回 True
    """
    try:
        if source_dict.__contains__(target_key) is True:
            if source_dict[target_key] is not None:
                if source_dict[target_key] != '':
                    return False
    except Exception as e:
        print('[ext_lib', '字典元素检查', str(e))
    return True
