# coding: utf-8
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny


class ArticleViewSet(GenericViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    @action(methods=["GET"], detail=False)
    def index(self, request, **kwargs):
        from .models import User
        a = User.objects.all().filter(name=1).filter(name=2)
        return Response('hello, {}'.format(settings.PROJECT_NAME))
