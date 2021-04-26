# -*- coding: utf-8 -*-
"""
微信登录获取OpenID和AccessToken

作者：张果
创建日期：2021-04-26
"""

import json

import requests


def get_access_token(code, client_type, client_label=None):
    """
    使用临时票据code获取openid和access_token

    参考链接：
    - 网站应用：https://developers.weixin.qq.com/doc/oplatform/Website_App/WeChat_Login/Wechat_Login.html

    :param code: 临时票据
    :param client_type: 微信应用类型，可选settings.QTAPP_CLIENT_TYPES
    :param client_label: 微信应用的标签
    :return:
    """
    # TODO: 验证client_label是否符合client_type

    # 根据client_type和client_label读取AppID和AppSecret
    if client_label is None:
        client_label = settings.WECHAT_LOGIN_DEFAULT_CLIENT_LABELS[client_type]
        wechat_client_secrets = settings.WECHAT_APP_SECRETS[client_label]
    else:
        wechat_client_secrets = settings.WECHAT_APP_SECRETS[client_label]
    appid = wechat_client_secrets['appid']
    secret = wechat_client_secrets['app_secret']

    # 拼接API的URL
    # 微信小程序使用小程序接口
    if client_type == 'mp':
        api_path = 'sns/jscode2session'
        code_type = 'js_code'
    # 网站应用、移动应用、微信公众号等使用OAuth2接口
    else:
        api_path = 'sns/oauth2/access_token'
        code_type = 'code'
    login_url: str = 'https://api.weixin.qq.com/{api_path}?appid={appid}&secret={secret}&{code_type}={code}&grant_type=authorization_code' \
        .format(api_path=api_path, appid=appid, secret=secret, code_type=code_type, code=code)

    # 请求微信登录服务器
    content = requests.get(login_url).content
    # 将json数据包转成字典
    response: dict = json.loads(content)

    if 'errcode' in response:
        # TODO: 定义异常类
        raise response

    return response