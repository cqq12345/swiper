
from django.core.cache import cache
from django.http import JsonResponse
from user.models import User

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
        return JsonResponse({'code':stat.SEND_SMS_ERROR,'data':None})

def submit_vcode(request):
    # 通过验证码登录,注册
    phonenum = request.POST.get('phonenum')
    vcode = request.POST.get('vcode')
    cache_Vcode=cache.get('Vcode_%s' % phonenum)#取出缓存的验证码
    if vcode and vcode == cache_Vcode:
        try:
            user=User.objects.get(phonenum=phonenum)
        except User.DoesNotExist:
            user=User.objects.create(phonenum=phonenum)#创建用户
            #进行登录
        request.session['uid']=user.id
        return JsonResponse({'code':stat.OK,'data':user.to_dict()})
    else:
        return JsonResponse({'code':stat.VCODE_ERROR,'data':None})



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
