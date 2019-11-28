import random

from django.core.cache import cache

from swiper import config

import requests
def gen_random_code(length=6):
    return ''.join([str(random.randint(0,9)) for i in range(length)])
def send_vcode(mobile):
    vcode=gen_random_code()#产生验证码

    print('状态码',vcode)
    args=config.YZX_SMS_ARGS.copy()#浅拷贝全局配置
    args['param']=vcode
    args['mobile']=mobile
    #调用第三方短信接口
    response=requests.post(config.YZX_SMS_API,json=args)
    if response.status_code == 200:
        result=response.json()
        if result['msg']=='OK':
            cache.set('Vcode_%s' % mobile, vcode, 180) #将验证码写入缓存，保存三分钟
            return True
        return False