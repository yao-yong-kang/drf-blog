from django.db import models
import uuid, os
from django.contrib.auth.models import User, AbstractBaseUser
from django.shortcuts import reverse



# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='分类名称')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name


def article_img_path(instance, filename):
    ext = filename.split('.')[-1]
    fielname = '{}{}'.format(uuid.uuid4(), ext)
    # return '{0}{1}{2}'.format(instance.user.id,"avatar",filename)
    return os.path.join("avatar", filename)


class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='文章标题')
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)
    img = models.ImageField(upload_to='article_img_path', null=True, blank=True, verbose_name='文章配图')
    content = models.TextField(verbose_name='文章内容')
    abstract = models.TextField(verbose_name='摘要', null=True, blank=True, max_length=255)
    visited = models.PositiveIntegerField(verbose_name='访问量', default=0)
    category = models.ManyToManyField('Category', verbose_name='文章分类')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章内容'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    # 调用函数 直接返回详情页的url地址ing
    def get_absolute_url(self):
        return reverse('blog:blog_detail', kwargs={'a_id': self.id})

    # 访问量加一
    def increase_visiting(self):
        self.visited += 1
        self.save(update_fields=['visited'])



