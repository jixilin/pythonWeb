# -*- coding: UTF-8 -*-
# @Time: 28/03/2018 4:42 PM
# Author: jixilin
# @Email: 1778202464@qq.com
from django.urls import path

from . import views

app_name = 'polls'  # 一个项目中有多个app时设置这个app的命名空间
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
