# coding: utf-8
from django.db.models import F
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny

from core.server.paginations import Pagination
from apps.content.models import Tag, Article


class TagViewSet(GenericViewSet, ListModelMixin):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Tag.objects.all()

    def list(self, request, *args, **kwargs):
        links = {}
        for a in Article.objects.filter(tags__isnull=False).values('id', 'tags'):
            for t in a['tags']:
                links[t] = links.get(t, 0) + 1

        queryset = self.filter_queryset(self.get_queryset()).values('id', 'name')
        data = []
        for t in queryset:
            link_num = links.get(str(t['id']), 0)
            if link_num > 0:
                data.append({'id': t['id'], 'name': t['name'], 'link_num': link_num})
        return Response(data)


class ArticleViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Article.objects.all().filter(online=True).order_by('-top', '-create_time')
    pagination_class = Pagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if request.GET.get('favorite'):
            # 按点赞数排序
            queryset = queryset.order_by('-like_num')
        if request.GET.get('tag'):
            # 按标签过滤
            queryset = queryset.filter(tags__icontains=request.GET.get('tag'))

        page = self.paginate_queryset(queryset.values('id', 'create_time', 'update_time', 'title', 'description',
                                                      'read_num', 'like_num', 'cover_type', 'cover', 'tags', 'top'))
        data = []
        for i in page:
            tag_infos = list(Tag.objects.filter(id__in=i['tags']).values('id', 'name'))
            data.append({"id": i['id'], "create_time": i['create_time'].strftime('%Y-%m-%d %H:%M:%S'),
                         "update_time": i['update_time'].strftime('%Y-%m-%d %H:%M:%S'),
                         "title": i['title'], "description": i['description'], "read_num": i['read_num'],
                         "like_num": i['like_num'], "cover": i['cover'], "cover_type": i['cover_type'],
                         "tags": tag_infos, 'top': 1 if i['top'] else 0})
        return self.get_paginated_response(data)

    def retrieve(self, request, *args, **kwargs):
        id = kwargs['pk']
        instance = Article.objects.filter(id=id).first()
        # 阅读数加一
        Article.objects.filter(id=id).update(read_num=F('read_num') + 1)
        tag_infos = []
        if instance.tags:
            tag_infos = list(Tag.objects.filter(id__in=instance.tags).values('id', 'name'))
        return Response({"id": instance.id, "create_time": instance.create_time.strftime('%Y-%m-%d %H:%M:%S'),
                         "update_time": instance.update_time.strftime('%Y-%m-%d %H:%M:%S'),
                         "title": instance.title, "description": instance.description, 'content': '',
                         "read_num": instance.read_num, "like_num": instance.like_num, "cover": instance.cover,
                         "cover_type": instance.cover_type, 'top': instance.top,
                         'content_format': instance.html_content,
                         "tags": tag_infos})

    @action(methods=['POST'], detail=True)
    def like(self, request, *args, **kwargs):
        """
        点赞数加一
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        Article.objects.filter(id=kwargs['pk']).update(like_num=F('like_num') + 1)
        return Response()
