# -*- coding: utf-8 -*-
"""
微信支付签名算法业务逻辑的实现

Ref:
  - https://zhuanlan.zhihu.com/p/402449405?utm_source=ZHShareTargetIDMore&utm_medium=social&utm_oi=78763203231744
"""

import base64
import time

from wechat_sdk.wechatpay_sdk.base.utils import gen_random_str, rs256_sign_with_pem, rs256_verify_with_pem


# ----- 生成签名 -----

def gen_sign_v2():
    """
    生成微信支付V2版本API签名
    :return:
    """
    pass


def gen_sign_v3(method, api, body, com_private_key_pem: bytes) -> bytes:
    """
    生成微信支付V3版本API签名
    :return:
    """
    # 构造签名串
    # https://wechatpay-api.gitbook.io/wechatpay-api-v3/qian-ming-zhi-nan-1/qian-ming-sheng-cheng#gou-zao-qian-ming-chuan
    current_timestamp_str: str = str(int(time.time()))
    nonce_str: str = gen_random_str(16)
    raw_sign_str: str = '\n'.join([method, api, current_timestamp_str, nonce_str, body])
    # 计算签名值
    # https://wechatpay-api.gitbook.io/wechatpay-api-v3/qian-ming-zhi-nan-1/qian-ming-sheng-cheng#gou-zao-qian-ming-chuan
    sign = base64.b64encode(rs256_sign_with_pem(raw_sign_str.encode('utf-8'), com_private_key_pem))
    return sign


# ----- 验证签名 -----

def verify_sign_v3(sign: bytes, wxp_public_key_pem: bytes) -> bool:
    """
    验证微信支付V3版本API签名

    Ref:
    - https://wechatpay-api.gitbook.io/wechatpay-api-v3/qian-ming-zhi-nan-1/qian-ming-yan-zheng#yan-zheng-qian-ming

    :return:
    """
    # base64解码
    decoded_sign = base64.b64decode(sign)
    return rs256_verify_with_pem(decoded_sign, wxp_public_key_pem)

