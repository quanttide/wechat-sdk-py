# -*- coding: utf-8 -*-

from wechat_sdk.wechatpay_sdk.base.client import WeChatPayBaseAPIClient


# ----- 类格式接口 ----

class WeChatPayOrderAPIClient(WeChatPayBaseAPIClient):
    def create_order(self):
        return self.request_api_v3(method='POST', api='pay/transaction')


# ----- 函数格式接口 -----

def create_wechatpay_order():
    client = WeChatPayOrderAPIClient()
    return client.create_order()
