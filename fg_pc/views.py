from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from common.models import User


def index(request):
    uid = request.session.get('uid', None)
    ctx = {'is_login': uid}
    return render(request, 'index.html', ctx)


def login(request):
    ctx = {}
    return render(request, 'login.html', ctx)


def error(request):
    ctx = {'title': '登录失败', 'msg': '用户名或密码错误'}
    return render(request, 'error.html', ctx)


def login_handler(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    row = User.objects.filter(username=username, password=password).first()
    if not row:
        return redirect(to='/error.html')
    else:
        request.session['uid'] = row.id
        return redirect(to='/')
