import datetime
from django.contrib import admin
from django.conf.urls import url

from core.server.admins import BaseModelAdmin
from .filters import AgeListFilter
from .models import Article


@admin.register(Article)
class ArticleAdmin(BaseModelAdmin):
    list_display = ('id', 'name', 'create_time')

    search_fields = ('name',)

    actions_on_top = True

    # 增加自定义按钮
    actions = ['custom_dialog']

    def get_urls(self):
        urls = super(ArticleAdmin, self).get_urls()
        my_urls = [
            url(r'^custom_dialog/$', self.admin_site.admin_view(self.custom_dialog), name='custom_dialog'),
        ]
        return my_urls + urls

    def custom_dialog(self, request):
        from django.http.response import JsonResponse
        return JsonResponse({'msg': 'sdf'})

    # 显示的文本，与django admin一致
    custom_dialog.short_description = '测试按钮'
    custom_dialog.url = '/admin/content/content/custom_dialog'
