# -*- coding: utf-8 -*-


from .base import WeChatPayBaseAPIClient


class WeChatPayAPIClient(WeChatPayBaseClient):
    def __init__(self):
        super(WeChatPayBaseAPIClient, self).__init__()