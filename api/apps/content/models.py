# coding: utf-8
from django.db import models


class Article(models.Model):
    name = models.CharField('demo名', max_length=20)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "文章管理"

    def __str__(self):
        return self.name
