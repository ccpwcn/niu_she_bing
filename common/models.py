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
