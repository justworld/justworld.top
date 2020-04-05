# coding: utf-8
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.conf import settings

admin.autodiscover()
admin.site.site_title = '管理后台'
admin.site.site_header = '管理后台'

# register
from apps import content_api_router
from apps.content.apis import ArticleViewSet, TagViewSet

content_api_router.register(r'article', ArticleViewSet, basename='article')
content_api_router.register(r'tag', TagViewSet, basename='tag')

urlpatterns = [
    url(r'^api/content/', include(content_api_router.urls)),
    path('{}/'.format(settings.ADMIN_PATH), admin.site.urls)
]
