import os
import time
from random import choice

import jieba
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from matplotlib.image import imread
from wordcloud import WordCloud

from common.models import User, DrawLog, FestivalGoods, Article


def index(request):
    uid = request.session.get('uid', None)
    ctx = {'is_login': 1}
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


def cloud(request):
    try:
        d = os.path.join(os.path.dirname(__file__), 'res')
        text = ''
        with open(os.path.join(d, 'language.text'), encoding='utf-8') as f:
            text = f.read()
        words = jieba.cut(text)
        words = " ".join(words)
        image_name = os.path.join(d, '草莓.jpg')  # 背景图片，也是词云的塑形图片
        coloring = imread(image_name)  # 读取图片
        font_name = "D:/fonts/Alibaba-PuHuiTi-Regular.ttf"
        word_cloud = WordCloud(
            mask=coloring,
            background_color='white',  # 白色背景
            font_path=font_name).generate(words)
        img = word_cloud.to_svg()
        ctx = {'title': '词云', 'img_data': img}
        return render(request, 'cloud.html', ctx)
    except Exception as e:
        ctx = {'title': '系统内部错误', 'msg': '如果您尝试多次仍然有问题，请联系琴心剑胆写代码'}
        return render(request, 'error.html', ctx)


def payment(request):
    try:
        with transaction.atomic():
            u = User(username='u1', nickname='user-1')
            u.save()
            a = Article(title='a1', content='article-1')
            a.save()
    except Exception as e:
        return JsonResponse(data={'code': 0, 'msg': '系统出现错误，请稍后重试'})
    return JsonResponse(data={'code': 0, 'msg': '成功'})


def action(request):
    # 查询
    day = time.localtime(time.time()).tm_mday
    n = DrawLog.objects.filter(user_id=1, create_time__day=day).count()
    print(n)

    # 新增
    dl = DrawLog(user_id=1, festival_goods_id=2)
    dl.save()

    # 更新
    u = User.objects.get(id=1)
    u.name = '琴心剑胆写代码'
    u.save()
