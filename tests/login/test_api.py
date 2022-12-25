# -*- coding: utf-8 -*-

import unittest
import os

from wechat_sdk.wechat_login_sdk.api import get_access_token, get_userinfo
from wechat_sdk.wechat_login_sdk.exception import WeChatLoginSDKException

# 本地测试获取环境变量
from environs import Env
Env().read_env()


class AccessTokenTestCase(unittest.TestCase):
    @unittest.skipIf(True, '需要云端部署以后才能测试')
    def test_get_access_token(self):
        pass

    def test_get_access_token_with_invalid_code(self):
        invalid_code = 'gegwesgargasa'
        with self.assertRaises(WeChatLoginSDKException) as e:
            get_access_token(os.environ.get('APPID'), os.environ.get('APPSECRET'), invalid_code)
        self.assertEqual(e.exception.errcode, '40029')


class UserInfoTestCase(unittest.TestCase):
    def test_get_user_info_with_invalid_access_token(self):
        invalid_openid = 'gesagsegaesg'
        invalid_access_token = 'gegsageesgaes'
        with self.assertRaises(WeChatLoginSDKException) as e:
            get_userinfo(invalid_openid, invalid_access_token)
        self.assertEqual(e.exception.errcode, '40014')


if __name__ == '__main__':
    unittest.main()
