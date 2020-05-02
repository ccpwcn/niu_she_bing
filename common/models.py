from django.db import models


# Create your models here.
class Article(models.Model):
    id = models.IntegerField('ID', default=0, primary_key=True)
    title = models.CharField('标题', max_length=100)
    sub_title = models.CharField('副标题', max_length=200)
    content = models.TextField('正文')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'article'


class Category(models.Model):
    id = models.IntegerField('ID', default=0, primary_key=True)
    name = models.CharField('名称', max_length=50)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'category'


class Tag(models.Model):
    id = models.IntegerField('ID', default=0, primary_key=True)
    name = models.CharField('名称', max_length=20)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'tag'


class User(models.Model):
    id = models.IntegerField('ID', default=0, primary_key=True)
    username = models.CharField('账号', max_length=20, null=False, default='')
    nickname = models.CharField('昵称', max_length=20, null=False, default='')
    password = models.CharField('密码', max_length=20, null=False, default='')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'user'


class FestivalGoods(models.Model):
    id = models.IntegerField('ID', default=0, primary_key=True)
    name = models.CharField('名称', max_length=20)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'festival_goods'


class DrawRule(models.Model):
    id = models.IntegerField('ID', default=0, primary_key=True)
    festival_goods_id = models.IntegerField('奖品')
    total_count = models.IntegerField('可用数量')
    used_count = models.IntegerField('已用数量')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'draw_rule'


class DrawLog(models.Model):
    id = models.IntegerField('ID', default=0, primary_key=True)
    user_id = models.IntegerField('用户')
    festival_goods_id = models.IntegerField('奖品')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'draw_log'


class CashInfo(models.Model):
    id = models.IntegerField('ID', default=0, primary_key=True)
    user_id = models.IntegerField('用户')
    festival_goods_id = models.IntegerField('奖品')
    status = models.IntegerField('兑现状态，1待发货，2已发货，3已签收，4已核验')
    receiver_name = models.CharField('收件人', max_length=20)
    receiver_mobile = models.CharField('收件人电话', max_length=20)
    receiver_address = models.CharField('收件人地址', max_length=200)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'cash_info'




