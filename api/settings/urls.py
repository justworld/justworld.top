# coding: utf-8
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

admin.autodiscover()
admin.site.site_title = '管理后台'
admin.site.site_header = '管理后台'

# register
from apps import api_router
from apps.content.apis import ArticleViewSet

api_router.register(r'article', ArticleViewSet, basename='article')

urlpatterns = [
    url(r'^api/', include(api_router.urls)),
    path('admin/', admin.site.urls)
]
