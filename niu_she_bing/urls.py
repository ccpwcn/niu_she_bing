"""niu_she_bing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import fg_pc.views

urlpatterns = [
    path('', fg_pc.views.index),
    path('login.html', fg_pc.views.login),
    path('login_handler.html', fg_pc.views.login_handler),
    path('error.html', fg_pc.views.error),
    path('admin/', admin.site.urls),
]
