# -*- coding: utf-8 -*-
"""

"""


class WeChatLoginSDKException(Exception):
    """
    TODO: 设计Exception类
     - 限制errcode的值的范围（-1，40029，45001），考虑使用枚举类型；
     - 优化errmsg，如果没有定制再用原始errmsg代替。
    """
    def __init__(self, errcode, errmsg):
        self.errcode = errcode
        self.errmsg = errmsg

    def __str__(self):
        return f'\n- error code: {self.errcode}\n- error message: {self.errmsg}'
