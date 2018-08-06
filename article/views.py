from django.shortcuts import render
from article.models import Home
from article.models import About
from article.models import Code
from article.forms import MomentForm
from django.http import HttpResponseRedirect
import os


def home(request):
    blog_list = Home.objects.all()  # 获取所有数据
    return render(request, 'index.html', {'blog_list': blog_list})   # 返回index.html页面


def about(request):
    about_content = About.objects.all
    return render(request, 'about.html', {'about_content': about_content})


def code(request):
    code_list = Code.objects.all()
    return render(request, 'code.html', {'code_list': code_list})


def moments_input(request):
    if request.method == 'POST':
        form = MomentForm(request.POST)
        if form.is_valid():
            moment = form.save()
            moment.save()
            return render(request, 'index.html', {'form': form})
    else:
        form = MomentForm()
        return render(request, 'index.html', {'form': form})