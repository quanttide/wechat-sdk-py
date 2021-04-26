# -*- coding: utf-8 -*-
"""
微信登录获取UnionID和用户信息

作者：张果
创建日期：2021-04-26
"""

import json

import requests


def get_userinfo(openid, access_token):
    """
    获取unionid和userinfo
    :param openid:
    :param access_token:
    :return:
    """
    user_info_url: str = 'https://api.weixin.qq.com/sns/userinfo?access_token={access_token}&openid={openid}' \
        .format(access_token=access_token, openid=openid)
    user_info: dict = json.loads(requests.get(user_info_url).content)
    return user_info