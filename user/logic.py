import random
import  os
from django.core.cache import cache

from swiper import config
from user.models import User

import requests

from libs.qn_clound import upload_to_qiniu
from tasks import celery_app


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
            cache.set('Vcode_%s' % mobile, vcode, 60000) #将验证码写入缓存，保存三分钟
            return True
        return False
def save_avatar(uid, avatar_file):
    '''将个人形象保存到本地'''
    filename = 'Avatar-%s' % uid
    filepath = '/tmp/%s' % filename
    with open(filepath, 'wb') as fp:
        for chunk in avatar_file.chunks():
            fp.write(chunk)
    return filename, filepath


@celery_app.task
def upload_avatar(uid, avatar_file):
    filename, filepath = save_avatar(uid, avatar_file)  # 文件保存到本地
    avatar_url = upload_to_qiniu(filename, filepath)  # 文件上传到七牛
    User.objects.filter(id=uid).update(avatars=avatar_url)  # 保存 URL
    os.remove(filepath)  # 删除本地临时文件