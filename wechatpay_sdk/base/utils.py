# -*- coding: utf-8 -*-
"""
可复用工具箱

Ref:
- Python实现：https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa.html
"""

import random
import string

from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature


# ----- 随机函数 -----

def gen_random_str(length: int) -> str:
    return ''.join(random.sample(string.ascii_letters + string.digits, length))


# ----- RS256算法 -----

def rs256_sign_with_pem(message: bytes, private_key_pem: bytes):
    """
    RS256签名算法，即SHA256 with RSA算法；私钥文件为pem格式的字节串

    @:param message: 待签名字符串
    @:param private_key_pem: 私钥pem文件路径
    :return:
    """
    private_key: rsa.RSAPrivateKey = load_pem_private_key(private_key_pem.encode('utf-8'))
    return private_key.sign(
        message,
        padding.PSS(
            mdf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )


def rs256_verify_with_pem(message: bytes, public_key_pem: bytes):
    """
    RS256签名验证算法；公钥文件为pem格式的字节串
    :param message:
    :param public_key_pem:
    :return:
    """
    public_key: rsa.RSAPublicKey = load_pem_public_key(public_key_pem)
    try:
        public_key.sign(
            message,
            padding.PSS(
                mdf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except InvalidSignature:
        return False
