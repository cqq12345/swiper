from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

from common import stat



class AuthMiddleware(MiddlewareMixin):
    '''用户登录中间件，白名单
        跳过这两个，要不然会重新加载所有的，
        不能产生sessionid
        '''
    path_white_list=[
        '/api/user/get_vcode',
        '/api/user/submit_vcode',
    ]
    def process_request(self,request):
        #检查当前路径是否在白名单中
        if request.path not in self.path_white_list:
            uid=request.session.get('uid')
            if not uid:
                return JsonResponse({'code':stat.LOGIN_REQURED,'data':None})
            else:
                request.uid=uid