# -*- coding: utf-8 -*-

from .base import BaseAPIClient


# ----- 类格式接口 ----

class TransactionAPIClient(BaseAPIClient):
    def create_order(self):
        return self.request_api_v3(method='POST', api='pay/transaction')


# ----- 函数格式接口 -----

def create_order():
    client = TransactionAPIClient()
    return client.create_order()
