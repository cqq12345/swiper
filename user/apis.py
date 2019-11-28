from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from user import logic

from common import stat
def get_vcode(request):
    # 获取短信验证
    phonenum = request.GET.get('phonenum')
    status = logic.send_vcode(phonenum)
    if status:
        return JsonResponse({'code':stat.OK,'data':None})
    else:
        return JsonResponse({'code':stat.VCODE_ERROR,'data':None})

def submit_vcode(request):
    # 通过验证码登录,注册

    return

def get_profile(request):
    # 获取个人资料
    return



def set_profile(request):
# 修改个人资料
    return

def upload_avatar(request):
    # 头像上传
    '''1.保存到本地
        2.上传到七牛云
         3.保存url
         4.删除本地'''


    return
