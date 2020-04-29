from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from common.models import Article


def index(request):
    page = int(request.GET.get('page', 1))
    page_size = int(request.GET.get('pageSize', 10))
    items = Article.objects.all()[(page - 1) * page_size : page * page_size]
    total = Article.objects.count()
    ctx = {'items': items, 'page': page, 'page_size': page_size, 'total': total}
    return render(request, 'index.html', ctx)
