from django.db import models

# Create your models here.


class Home(models.Model):
    title = models.CharField(max_length=150)    # 博客标题
    body = models.TextField()                   # 博客正文
    timestamp = models.DateTimeField()          # 创建时间

    def __str__(self):
        return self.title


class About(models.Model):
    body = models.TextField()


class Code(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()

    def __str__(self):
        return self.title