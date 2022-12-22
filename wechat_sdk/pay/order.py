# -*- coding: utf-8 -*-


class WeChatPayOrderAPIMixin:
    def create_order(self):
        return self.request_api(method='POST', api='pay/transaction')
