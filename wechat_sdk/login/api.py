# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
微信登录服务端API

作者：张果
创建日期：2021-06-11
"""

import requests

from wechat_sdk.wechat_login_sdk.exception import WeChatLoginSDKException


def get_access_token(appid: str, app_secret: str, code: str, is_mp: bool = False) -> dict:
    """
    使用临时票据code获取openid和access_token/session_key等，其中：
    - 网站和移动应用使用OAuth2登录，返回access_token接口调用凭证，用以调用微信API时鉴权。
    - 小程序调用小程序专用API登录，返回session_key会话密钥，用以完成小程序登录鉴权。

    API接口规则详见：
    - 网站应用：https://developers.weixin.qq.com/doc/oplatform/Website_App/WeChat_Login/Wechat_Login.html
    - 移动应用：https://developers.weixin.qq.com/doc/oplatform/Mobile_App/WeChat_Login/Development_Guide.html
    - 小程序：https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/login/auth.code2Session.html

    :param appid: 微信公众号/小程序的AppId。
    :param app_secret: 微信公众号/小程序的AppSecret。
    :param code: 客户端通过微信登录API获取的临时票据CODE。
    :param is_mp: 是否为小程序，默认为否。
    :return: 微信分配给用户的ID及用于微信API的鉴权凭证等，具体为：
      - OAuth2：
        - unionid: 微信用户在绑定到同一个微信开放平台的不同应用（一般属于同一个主体）的唯一ID，用户授权userinfo时返回。
        - openid: 微信用户在同一个微信应用下的唯一ID，同一主体的不同微信公众号/小程序不同。
        - access_token: 微信API调用凭证。
        - expires_in: access_token接口调用凭证超时时间，单位秒，默认为7200秒。（TODO：审视是否需要返回）
        - refresh_token: 用以刷新access_token。
        - scope: 用户授权的作用域，使用逗号（,）分隔。（TODO：进一步改进格式，考虑使用枚举类型）
      - 小程序：
        - unionid: 同OAuth2模式，小程序绑定开放平台时返回。
        - openid: 同OAuth2模式。
        - session_key: 会话密钥，类似于OAuth2的access_token。
    """
    # 拼接API的URL
    # 微信小程序使用小程序接口
    if is_mp:
        api_path = 'sns/jscode2session'
        code_type = 'js_code'
    # 网站应用、移动应用、微信公众号等使用OAuth2接口
    else:
        api_path = 'sns/oauth2/access_token'
        code_type = 'code'
    login_url: str = 'https://api.weixin.qq.com/{api_path}?appid={appid}&secret={secret}&{code_type}={code}&grant_type=authorization_code' \
        .format(api_path=api_path, appid=appid, secret=app_secret, code_type=code_type, code=code)

    # 请求微信登录服务器
    # TODO: 如有必要，处理网络请求的异常码
    r = requests.get(login_url)
    # 将json数据包转成字典
    data: dict = r.json()

    if 'errcode' in data and data['errcode'] != '0':
        raise WeChatLoginSDKException(data['errcode'], data['errmsg'])
    return data


def get_userinfo(openid, access_token):
    """
    获取unionid和userinfo
    :param openid:
    :param access_token:
    :return:
    """
    user_info_url: str = 'https://api.weixin.qq.com/sns/userinfo?access_token={access_token}&openid={openid}' \
        .format(access_token=access_token, openid=openid)
    data: dict = requests.get(user_info_url).json()

    if 'errcode' in data and data['errcode'] != '0':
        raise WeChatLoginSDKException(data['errcode'], data['errmsg'])
    return data
