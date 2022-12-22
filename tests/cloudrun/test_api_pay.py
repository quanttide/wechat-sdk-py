import unittest
import responses

from wechat_sdk.cloudrun.api.pay import WXCloudRunPayAPIClient


class WXCloudRunPayTestCase(unittest.TestCase):
    def setUp(self):
        self.client = WXCloudRunPayAPIClient()

    def test_request_pay_api(self):
        pass

    @responses.activate
    def test_unifiedorder(self):
        responses.post("http://api.weixin.qq.com/_/pay/unifiedorder", json={"errcode": 0, "errmsg": "ok",
            "respdata": {"return_code": "SUCCESS", "return_msg": "OK", "appid": "wxd2565e6a04246fd1",
                         "mch_id": "1800780001", "sub_appid": "wxd2565e6a04246fd1", "sub_mch_id": "1712734762",
                         "nonce_str": "BfM1ojiTfFCbpmkL", "sign": "00F0CB2E2491AD98CF0A5817002B8962",
                         "result_code": "SUCCESS", "trade_type": "JSAPI",
                         "prepay_id": "wx29415831e6a111ccb805125015a7282000",
                         "payment": {"appId": "wxd2565e6a04246fd1", "timeStamp": "1647841885",
                                     "nonceStr": "BfM1ojiTfFCbpmkL",
                                     "package": "prepay_id=wx2825019415cb82821e6a15a7c113510000", "signType": "MD5",
                                     "paySign": "038EE415FD025B0D37717E8A1D6C34B6"}}})
        data = {"body": "测试微信支付", "openid": "oZp5njTTsWaCeEoXi14oeOVCKlik",
            "out_trade_no": "2021WERUN1647840687637", "spbill_create_ip": "59.37.125.120",
            "env_id": "prod-66733tes755tabc", "sub_mch_id": "1712734762", "total_fee": 1, "callback_type": 2,
            "container": {"service": "pay", "path": "/"}}
        resp = self.client.unifiedorder(data)
        print(resp)


if __name__ == '__main__':
    unittest.main()
