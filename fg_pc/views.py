import time
from random import choice

from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from common.models import User, DrawLog, FestivalGoods


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


def draw_start(request):
    uid = request.session.get('uid', None)
    day = time.localtime(time.time()).tm_mday
    n = DrawLog.objects.filter(user_id=uid, create_time__day=day).count()
    if n > 2:  # 卡死这个环节，有2条数据时，无论如何都不能再抽了
        return JsonResponse(data={'code': 1, 'msg': '您已经抽过奖了，不能再抽了'})
    else:
        row = DrawLog.objects.filter(user_id=uid, create_time__day=day).first()
        if not row or row.festival_goods_id == 4:
            return JsonResponse(data={'code': 0, 'msg': '抽奖中'})
        else:
            return JsonResponse(data={'code': 1, 'msg': '您已经抽过奖了，不能再抽了'})


def draw_end(request):
    uid = request.session.get('uid', None)
    day = time.localtime(time.time()).tm_mday
    n = DrawLog.objects.filter(user_id=uid, create_time__day=day).count()
    if n > 2:  # 卡死这个环节，有2条数据时，无论如何都不能再抽了
        return JsonResponse(data={'code': 1, 'msg': '您已经抽过奖了，不能再抽了'})
    else:
        row = DrawLog.objects.filter(user_id=uid, create_time__day=day).first()
        if not row or row.festival_goods_id == 4:
            goods = FestivalGoods.objects.all()
            target = choice(goods)
            dl = DrawLog(user_id=uid, festival_goods_id=target.id)
            dl.save()
            d = {'code': 0, 'msg': '抽奖完成', 'data': {'id': target.id, 'name': target.name, 'desc': target.desc}, 'draw_log_id': dl.id}
            return JsonResponse(data=d)
        else:
            return JsonResponse(data={'code': 1, 'msg': '您已经抽过奖了，不能再抽了'})
