from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin


class AuthMiddleware(MiddlewareMixin):
    no_check_urls = [
        '/login.html',
        '/login_handler.html',
        '/error.html'
    ]

    def process_request(self, request):
        if request.path in self.no_check_urls:
            # 对部分页面放行
            return None
        uid = request.session.get('uid', None)
        if not uid:
            return HttpResponseRedirect('/login.html')
        return None

    def process_response(self, request, response):
        return response
