"""
定义服务返回信息列表
"""


def response(code='default', msg='default', data=None):
    res = {
        'code': code,
        'msg': msg
    }
    if data is not None:
        res['data'] = data
    return res


def success(data=None):
    return response('2000', 'success', data)


def error(data=None):
    return response('5000', 'error', data)


def sys_error(code='9001'):
    code_list = {
        '9001': 'Socket creation failed!',
        '9002': 'Socket bind failed!',
        '9003': 'Registry send failed!',
    }
    return {'code': code, 'msg': code_list[code]}
