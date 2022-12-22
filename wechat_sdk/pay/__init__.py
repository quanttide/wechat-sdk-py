# -*- coding: utf-8 -*-


from .base import WeChatPayBaseAPIClient
from .order import WeChatPayOrderAPIMixin


class WeChatPayAPIClient(
    WeChatPayBaseAPIClient,
    WeChatPayOrderAPIMixin
):
    pass
