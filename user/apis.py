
from django.core.cache import cache

from user.models import User

# Create your views here.
from user import logic

from common import stat

from user.models import Profile

from libs.http import render_json

from user.Form import UserForm
from user.Form import ProfileForm




def get_vcode(request):
    # 获取短信验证
    phonenum = request.GET.get('phonenum')
    status = logic.send_vcode(phonenum)
    if status:
        return render_json()
    else:
        return render_json(code=stat.SEND_SMS_ERROR)

def submit_vcode(request):
    # 通过验证码登录,注册
    phonenum = request.POST.get('phonenum')
    vcode = request.POST.get('vcode')
    cache_vcode=cache.get('Vcode_%s' % phonenum)#取出缓存的验证码
    if vcode and vcode == cache_vcode:
        try:
            user=User.objects.get(phonenum=phonenum)
        except User.DoesNotExist:
            user=User.objects.create(phonenum=phonenum)#创建用户
            #进行登录
        request.session['uid']=user.id
        return render_json(data=user.to_dict())
    else:
        return render_json(code=stat.VCODE_ERROR)



def get_profile(request):
    # 获取个人资料
    profile,_=Profile.objects.get_or_create(id=request.uid)
    return render_json(data=profile.to_dict())



def set_profile(request):
    '''修改个人资料'''
    user_form=UserForm(request.POST)
    profile_form = ProfileForm(request.POST)

    # 检查数据有效性
    if not user_form.is_valid():
        return render_json(user_form.errors, stat.USER_FORM_ERROR)
    if not profile_form.is_valid():
        return render_json(profile_form.errors, stat.USER_FORM_ERROR)

    # 保存数据
    User.objects.filter(id=request.uid).update(**user_form.cleaned_data)
    Profile.objects.filter(id=request.uid).update(**profile_form.cleaned_data)
    return render_json()

def upload_avatar(request):
    # 头像上传
    '''1.保存到本地
        2.上传到七牛云
         3.保存url
         4.删除本地'''
    avatar_file = request.FILES.get('avatars')
    logic.upload_avatar.delay(request.uid, avatar_file)
    return render_json()


