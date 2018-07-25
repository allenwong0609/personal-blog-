from django.contrib import admin

# Register your models here.
from django.contrib import admin
from article.models import Home
from article.models import About
from article.models import Code


# Register your models here.
class HomeAdmin(admin.ModelAdmin):
    list_display1 = ['title', 'body', 'timestamp']


class AboutAdmin(admin.ModelAdmin):
    list_display2 = ['body']


class CodeAdmin(admin.ModelAdmin):
    list_display3 = ['title', 'content']

admin.site.register(Home, HomeAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Code, CodeAdmin)