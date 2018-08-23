from django.shortcuts import render
from .models import Topic_1, Topic_2, Topic_3, Topic_4
# Create your views here.

def index(request):
    """博客的主页"""
    return render(request, 'my_blogs/index.html')

def topics1(request):
    """显示主题一"""
    topics1 = Topic_1.objects.order_by('date_added')
    context = {'topics1': topics1}
    return render(request, 'my_blogs/topics1.html', context)

def topics2(request):
    """显示主题一"""
    topics2 = Topic_2.objects.order_by('date_added')
    context = {'topics2': topics2}
    return render(request, 'my_blogs/topics2.html', context)

def topics3(request):
    """显示主题一"""
    topics3 = Topic_3.objects.order_by('date_added')
    context = {'topics3': topics3}
    return render(request, 'my_blogs/topics3.html', context)

def topics4(request):
    """显示主题一"""
    topics4 = Topic_4.objects.order_by('date_added')
    context = {'topics4': topics4}
    return render(request, 'my_blogs/topics4.html', context)


def topic1(request, topic1_id):
    """显示单个主题及其所有的条目"""
    topic1 = Topic_1.objects.get(id=topic1_id)
    entries1 =topic1.entry_set.order_by('-date_added')
    context = {'topic1': topic1, 'entries1': entries1}
    return render(request, 'my_blogs/topic1.html', context)



