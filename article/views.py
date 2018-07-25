from django.shortcuts import render
from article.models import Home
from article.models import About
from article.models import Code


def home(request):
    blog_list = Home.objects.all()  # 获取所有数据
    return render(request, 'index.html', {'blog_list': blog_list})   # 返回index.html页面


def about(request):
    about_content = About.objects.all
    return render(request, 'about.html', {'about_content': about_content})


def code(request):
    code_list = Code.objects.all()
    return render(request, 'code.html', {'code_list': code_list})