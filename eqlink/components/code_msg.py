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
