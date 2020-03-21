# coding: utf-8
from django.contrib import admin


class BaseModelAdmin(admin.ModelAdmin):
    # 分页显示，一页的数量
    list_per_page = 10

