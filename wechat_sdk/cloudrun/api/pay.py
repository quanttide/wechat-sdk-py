"""
微信支付API

官方文档：https://developers.weixin.qq.com/miniprogram/dev/wxcloudrun/src/guide/weixin/pay.html
"""

import requests


class WXCloudRunPayAPIClient:
    """
    TODO: 确认云开发为同一套API，整体移到cloud模块并为云开发和云托管暴露上层API。
    """
    def request_pay_api(self, api_name: str, data: dict, openid: str = None):
        """

        官方文档：https://developers.weixin.qq.com/miniprogram/dev/wxcloudrun/src/guide/weixin/pay.html

        :param api_name: 接口名称
        :param data:
        :param openid:
        :return:
        """
        # > 使用开放接口服务，通过POST请求微信支付接口`/_/pay/`接口名称，从而调用微信支付能力。
        url = f"http://api.weixin.qq.com/_/pay/{api_name}"
        # > 对于需要OpenID的接口，需要在JSON顶层加入OpenID字段
        if openid:
            data['openid'] = openid
        r = requests.request('POST', url, data=data)
        return_data = r.json()
        if int(return_data['errcode']) == 0 and return_data['errmsg'] == 'ok':
            return return_data['respdata']

    def unifiedorder(self, data):
        return self.request_pay_api(api_name='unifiedorder', data=data)
