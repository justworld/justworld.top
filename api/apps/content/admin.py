import datetime
from django.contrib import admin
from django.conf.urls import url

from core.server.admins import BaseModelAdmin
from .filters import AgeListFilter
from .models import Tag, Article
from .forms import ArticleForm


@admin.register(Tag)
class TagAdmin(BaseModelAdmin):
    list_display = ('id', 'name', 'online', 'create_time', 'update_time')
    search_fields = ('name',)
    actions_on_top = True


@admin.register(Article)
class ArticleAdmin(BaseModelAdmin):
    list_display = ('id', 'title', 'description', 'cover_type', 'tags', 'online', 'top', 'read_num', 'like_num',
                    'create_time', 'update_time')
    exclude = ('read_num', 'like_num', 'create_time', 'update_time')
    search_fields = ('title',)
    actions_on_top = True
    form = ArticleForm

    def get_select_tags(self, *args, **kwargs):
        """
        获取可选的标签数据
        :return queryset
        """
        return Tag.objects.all()
