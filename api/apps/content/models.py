# coding: utf-8
from django.db import models

from core.database.models import FilteredMultiSelectField
from apps.constants import CoverType


class Tag(models.Model):
    name = models.CharField('标签名', max_length=20)
    online = models.BooleanField('是否上线', default=False)

    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "标签管理"
        app_label = 'content'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField('标题', max_length=50)
    description = models.CharField('描述', max_length=100)
    html_content = models.TextField('内容', blank=True)
    cover_type = models.SmallIntegerField('封面类型', choices=CoverType())
    cover = models.CharField('封面', max_length=255)
    tags = FilteredMultiSelectField('所属标签', max_length=100)
    online = models.BooleanField('是否上线', default=False)
    top = models.BooleanField('是否置顶', default=False)
    read_num = models.IntegerField('阅读数', default=0)
    like_num = models.IntegerField('点赞数', default=0)

    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "文章管理"
        app_label = 'content'

    def __str__(self):
        return self.title
