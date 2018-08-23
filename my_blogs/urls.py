from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index, name='index'),

    #显示主题一
    path('topics1/', views.topics1, name='topics1'),
    # 显示主题1的详细页面
    re_path('topics1/(?P<topic1_id>\d+)/', views.topic1, name='topic1'),

    #显示主题二
    path('topics2/', views.topics2, name='topics2'),

    #显示主题三
    path('topics3/', views.topics3, name='topics3'),

    #显示主题四
    path('topics4/', views.topics4, name='topics4'),


]
app_name = 'my_blogs'