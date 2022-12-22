# -*- coding: utf-8 -*-

import requests

from wechat_sdk.wechatpay_sdk.base.sign import gen_sign_v3


class WeChatPayBaseAPIClient(object):
    def __init__(self, mch_id, serial_no, com_private_key_path):
        self.mch_id = mch_id
        self.serial_no = serial_no
        self.api_root_url_v3 = 'https://api.mch.weixin.qq.com/v3/'
        self.auth_type_v3 = 'WECHATPAY2-SHA256-RSA2048'
        with open(com_private_key_path) as f:
            self.com_private_key_pem = f.read()

    def gen_sign_v3(self, method, api, body):
        """
        注意：V3版本接口需要为每次请求量身定做一个签名
        :param method:
        :param api:
        :param body:
        :return:
        """
        return gen_sign_v3(method, api, body, self.com_private_key_pem.encode('utf-8'))

    def request_api_v3(self, method, api, body):
        # 生成URL
        url = self.api_root_url_v3 + api
        # 生成签名
        sign = gen_sign_v3(method, api, body)
        # 生成认证信息
        auth_value = "mchid={mchid},nonce_str={nonce_str}".format(mchid=self.mch_id)  # TODO
        auth = self.auth_type_v3 + '' + auth_value
        # 生成请求头
        headers = {'Authorization': auth}
        # 发送请求
        # TODO: POST请求传入body，GET请求body为空
        response = requests.request(method, url, headers=headers)
        return response.data

    def request_api(self, *args, **kwargs):
        return self.request_api_v3(*args, **kwargs)
