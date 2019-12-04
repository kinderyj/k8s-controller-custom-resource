# coding:utf-8
from __future__ import unicode_literals, print_function

import hashlib
import hmac
import random
import time
import datetime
import base64


def unique_random_number():
    now_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    random_num = random.randint(0, 100)
    if random_num <= 10:
        random_num = str(0) + str(random_num)
    unique_num = str(now_time) + str(random_num)
    return unique_num


def create_hmac_sha256_signature(secret_id, secret_key):
    #"""hmac_sha256ǩ"
    time_stamp = str(int(round(time.time()*1000)))
    uniq_random = unique_random_number()
    message = uniq_random + secret_id + time_stamp
    signature_binary = hmac.new(secret_key.encode('utf-8'), message.encode('utf-8'), hashlib.sha256).digest()
    signature_base64 = base64.b64encode(signature_binary)
    return signature_base64, uniq_random, time_stamp  #  signature 


if __name__ == '__main__':
    api_id = 'sys_common_query'
    api_secret = '18NPlBi46XnDyXeroLeiuc11'
    signature, nonce, timestamp = create_hmac_sha256_signature(api_id, api_secret)
    print(signature)
    print(nonce)
    print(timestamp)
    
