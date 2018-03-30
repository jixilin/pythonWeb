# -*- coding: UTF-8 -*-
# @Time: 28/03/2018 3:08 PM
# Author: jixilin
# @Email: 1778202464@qq.com
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
