# -*- coding: utf-8 -*-


from .base import BaseAPIClient
from .pay import TransactionAPIClient


class WeChatPayAPIClient(BaseAPIClient, TransactionAPIClient):
    def __init__(self):
        super(WeChatPayBaseAPIClient, self).__init__()