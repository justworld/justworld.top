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
        queryset = self.filter_queryset(self.get_queryset())
        data = [{'id': t.id, 'name': t.name, 'link_num': 1} for t in queryset]
        return Response(data)


class ArticleViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Article.objects.all().filter(online=True)
    pagination_class = Pagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if request.GET.get('favorite'):
            # 按点赞数排序
            queryset = queryset.order_by('-like_num')

        page = self.paginate_queryset(queryset.values('id', 'create_time', 'update_time', 'title', 'description',
                                                      'read_num', 'like_num', 'cover_type', 'cover', 'tags'))
        data = []
        for i in page:
            tag_infos = list(Tag.objects.filter(id__in=i['tags']).values('id', 'name'))
            data.append({"id": i['id'], "create_time": i['create_time'], "update_time": i['update_time'],
                         "title": i['title'], "description": i['description'], "read_num": i['read_num'],
                         "like_num": i['like_num'], "cover": i['cover'], "cover_type": i['cover_type'],
                         "tags": tag_infos})
        return self.get_paginated_response(data)

    def retrieve(self, request, *args, **kwargs):
        id = kwargs['pk']
        instance = Article.objects.filter(id=id).first()
        # 阅读数加一
        Article.objects.filter(id=id).update(read_num=F('read_num') + 1)
        tag_infos = []
        if instance.tags:
            tag_infos = list(Tag.objects.filter(id__in=instance.tags).values('id', 'name'))
        return Response({"id": instance.id, "create_time": instance.create_time, "update_time": instance.update_time,
                         "title": instance.title, "description": instance.description, 'content': instance.content,
                         "read_num": instance.read_num, "like_num": instance.like_num, "cover": instance.cover,
                         "cover_type": instance.cover_type, 'top': instance.top,
                         'content_format': instance.content_format,
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
