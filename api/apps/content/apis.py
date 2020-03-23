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
    pagination_class = Pagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page_queryset = self.paginate_queryset(queryset)
        if page_queryset is not None:
            data = [{'id': t.id, 'name': t.name, 'link_num': 1} for t in page_queryset]
            return self.get_paginated_response(data)

        return Response()


class ArticleViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Article.objects.all().filter(online=True)
    pagination_class = Pagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        data = {"count": 52, "page_size": 15, "total_page": 4, "page": 1,
                "list": [{"id": 1, "createTime": 1552151378000, "updateTime": None,
                          "title": "关于本站和博主", "description": "关于本站和博主",
                          "author": "Bobbi", "content": None, "readNum": 5221,
                          "likeNum": 14102,
                          "cover": "http://oss.dblearn.cn/dbblog/20190303/18a6c1d2ed47494396462901ffe02f30.jpg",
                          "coverType": 1, "recommend": None, "categoryId": None,
                          "publish": None, "top": True, "contentFormat": None,
                          "tagList": [{"id": 1, "name": "本站相关", "type": 0},
                                      {"id": 2, "name": "关于", "type": 0}]},
                         {"id": 60, "createTime": 1584170805000, "updateTime": None,
                          "title": "这是一个招聘帖，内推！",
                          "description": "阿里新零售供应链招聘啦，社招校招岗位都有，欢迎来投",
                          "author": "Bobbi", "content": None, "readNum": 90,
                          "likeNum": 10, "cover": None, "coverType": 2,
                          "recommend": None, "categoryId": None, "publish": None,
                          "top": False, "contentFormat": None,
                          "tagList": [{"id": 29, "name": "招聘", "type": 0}]},
                         {"id": 58, "createTime": 1574578028000, "updateTime": None,
                          "title": "Java多线程JUC锁11——AbstractQueuedSynchronizer详解(3)",
                          "description": "AQS为继承它的实现类提供基础设施，如构建等待队列、控制同步状态等；其内部除了提供并发操作的核心方法以及等待队列操作外，还提供了一些模板方法让子类自己实现，AQS只关注内部公共方法实现，并不关心外部不同模式的实现。",
                          "author": "Bobbi", "content": None, "readNum": 274,
                          "likeNum": 130, "cover": None, "coverType": 2,
                          "recommend": None, "categoryId": None, "publish": None,
                          "top": False, "contentFormat": None,
                          "tagList": [{"id": 7, "name": "Java", "type": 0},
                                      {"id": 24, "name": "JUC锁", "type": 0}]},
                         {"id": 56, "createTime": 1573972105000, "updateTime": None,
                          "title": "Java多线程JUC锁10——AbstractQueuedSynchronizer详解(2)",
                          "description": "AQS为继承它的实现类提供基础设施，如构建等待队列、控制同步状态等；其内部除了提供并发操作的核心方法以及等待队列操作外，还提供了一些模板方法让子类自己实现，AQS只关注内部公共方法实现，并不关心外部不同模式的实现。",
                          "author": "Bobbo", "content": None, "readNum": 148,
                          "likeNum": 105, "cover": None, "coverType": 2,
                          "recommend": None, "categoryId": None, "publish": None,
                          "top": False, "contentFormat": None,
                          "tagList": [{"id": 7, "name": "Java", "type": 0},
                                      {"id": 24, "name": "JUC锁", "type": 0}]},
                         {"id": 55, "createTime": 1573401014000, "updateTime": None,
                          "title": "Java多线程JUC线程池06——ScheduledThreadPoolExecutor详解(2)",
                          "description": "ScheduledThreadPoolExecutor用于执行周期性或延时性的定时任务，它是在ThreadPoolExecutor的基础上实现的任务调度线程池，内部使用延时工作队列DelayedWorkQueue实现对任务的延时调度。",
                          "author": "Bobbi", "content": None, "readNum": 144,
                          "likeNum": 25, "cover": None, "coverType": 2,
                          "recommend": None, "categoryId": None, "publish": None,
                          "top": False, "contentFormat": None,
                          "tagList": [{"id": 7, "name": "Java", "type": 0},
                                      {"id": 28, "name": "JUC线程池", "type": 0}]},
                         {"id": 54, "createTime": 1572108862000, "updateTime": None,
                          "title": "Java多线程JUC线程池05——ScheduledThreadPoolExecutor详解(1)",
                          "description": "ScheduledThreadPoolExecutor用于执行周期性或延时性的定时任务，它是在ThreadPoolExecutor的基础上实现的任务调度线程池，内部使用延时工作队列DelayedWorkQueue实现对任务的延时调度",
                          "author": "Bobbi", "content": None, "readNum": 162,
                          "likeNum": 16, "cover": None, "coverType": 2,
                          "recommend": None, "categoryId": None, "publish": None,
                          "top": False, "contentFormat": None,
                          "tagList": [{"id": 7, "name": "Java", "type": 0},
                                      {"id": 28, "name": "JUC线程池", "type": 0}]},
                         {"id": 53, "createTime": 1572034845000, "updateTime": None,
                          "title": "Java多线程JUC线程池04——Callable、Future、FutureTask",
                          "description": "Runnable接口是针对单纯的无返回值任务，当我们需要获取线程的执行结果时，就需要用到它们。Callable用于产生结果，Future用于获取结果。",
                          "author": "Bobbi", "content": None, "readNum": 119,
                          "likeNum": 21, "cover": None, "coverType": 2,
                          "recommend": None, "categoryId": None, "publish": None,
                          "top": False, "contentFormat": None,
                          "tagList": [{"id": 7, "name": "Java", "type": 0},
                                      {"id": 28, "name": "JUC线程池", "type": 0}]},
                         {"id": 52, "createTime": 1572003126000, "updateTime": None,
                          "title": "Java多线程JUC线程池03——ThreadPoolExecutor解析(2)",
                          "description": "上一节中介绍了线程池的生命周期和数据结构，本章会通过分析线程池的源码，对线程池进行说明",
                          "author": "Bobbi", "content": None, "readNum": 99,
                          "likeNum": 53, "cover": None, "coverType": 2,
                          "recommend": None, "categoryId": None, "publish": None,
                          "top": False, "contentFormat": None,
                          "tagList": [{"id": 7, "name": "Java", "type": 0},
                                      {"id": 28, "name": "JUC线程池", "type": 0}]},
                         {"id": 51, "createTime": 1571874930000, "updateTime": None,
                          "title": "Java多线程JUC线程池02——ThreadPoolExecutor解析(1)",
                          "description": "ThreadPoolExecutor是线程池类。对于线程池，可以通俗的将它理解为\"存放一定数量线程的一个线程集合。线程池允许若个线程同时允许，允许同时运行的线程数量就是线程池的容量；当添加的到线程池中的线程超过它的容量时，会有一部分线程阻塞等待。线程池会通过相应的调度策略和拒绝策略，对添加到线程池中的线程进行管理。",
                          "author": "Bobbi", "content": None, "readNum": 99,
                          "likeNum": 71, "cover": None, "coverType": 2,
                          "recommend": None, "categoryId": None, "publish": None,
                          "top": False, "contentFormat": None,
                          "tagList": [{"id": 7, "name": "Java", "type": 0},
                                      {"id": 28, "name": "JUC线程池", "type": 0}]},
                         {"id": 50, "createTime": 1571853810000, "updateTime": None,
                          "title": "Java多线程JUC线程池01——线程池架构",
                          "description": "介绍JUC线程池架构及其示例", "author": "Bobbi",
                          "content": None, "readNum": 113, "likeNum": 12,
                          "cover": None, "coverType": 2, "recommend": None,
                          "categoryId": None, "publish": None, "top": False,
                          "contentFormat": None,
                          "tagList": [{"id": 7, "name": "Java", "type": 0},
                                      {"id": 28, "name": "JUC线程池", "type": 0}]},
                         {"id": 49, "createTime": 1571261499000, "updateTime": None,
                          "title": "Java多线程JUC锁09——AbstractQueuedSynchronizer详解(1)",
                          "description": "AQS为继承它的实现类提供基础设施，如构建等待队列、控制同步状态等；其内部除了提供并发操作的核心方法以及等待队列操作外，还提供了一些模板方法让子类自己实现，AQS只关注内部公共方法实现，并不关心外部不同模式的实现。",
                          "author": "Bobbi", "content": None, "readNum": 122,
                          "likeNum": 84, "cover": None, "coverType": 2,
                          "recommend": None, "categoryId": None, "publish": None,
                          "top": False, "contentFormat": None,
                          "tagList": [{"id": 7, "name": "Java", "type": 0},
                                      {"id": 24, "name": "JUC锁", "type": 0}]},
                         {"id": 47, "createTime": 1569798094000, "updateTime": None,
                          "title": "SpringBoot自动配置源码解析",
                          "description": "SpringBoot的出现可谓是大大提升了Java的开发体验。它集成了大量常用的第三方库配置，Spring Boot应用中这些第三方库几乎可以是零配置的开箱即用，大部分的 Spring Boot 应用都只需要非常少量的配置代码（基于 Java 的配置），开发者能够更加专注于业务逻辑。",
                          "author": "Bobbi", "content": None, "readNum": 156,
                          "likeNum": 15, "cover": None, "coverType": 2,
                          "recommend": None, "categoryId": None, "publish": None,
                          "top": False, "contentFormat": None,
                          "tagList": [{"id": 7, "name": "Java", "type": 0},
                                      {"id": 27, "name": "SpringBoot", "type": 0}]},
                         {"id": 46, "createTime": 1569077582000, "updateTime": None,
                          "title": "Java集合07——HashMap",
                          "description": "HashMap 是一个散列表，它存储的内容是键值对(key-value)映射",
                          "author": "Bobbi", "content": None, "readNum": 151,
                          "likeNum": 78, "cover": None, "coverType": 2,
                          "recommend": None, "categoryId": None, "publish": None,
                          "top": False, "contentFormat": None,
                          "tagList": [{"id": 26, "name": "Java集合", "type": 0},
                                      {"id": 7, "name": "Java", "type": 0}]},
                         {"id": 45, "createTime": 1569065451000, "updateTime": None,
                          "title": "Java集合06——Map框架",
                          "description": "Map 是一个键值对(key-value)映射接口。Map映射中不能包含重复的键；每个键最多只能映射到一个值",
                          "author": "Bobbi", "content": None, "readNum": 66,
                          "likeNum": 2, "cover": None, "coverType": 2,
                          "recommend": None, "categoryId": None, "publish": None,
                          "top": False, "contentFormat": None,
                          "tagList": [{"id": 7, "name": "Java", "type": 0},
                                      {"id": 26, "name": "Java集合", "type": 0}]},
                         {"id": 44, "createTime": 1568897710000, "updateTime": None,
                          "title": "Java集合05——LinkedList",
                          "description": "LinkedList 是一个继承于AbstractSequentialList的双向链表。它也可以被当作堆栈、队列或双端队列进行操作。",
                          "author": "Bobbi", "content": None, "readNum": 62,
                          "likeNum": 0, "cover": None, "coverType": 2,
                          "recommend": None, "categoryId": None, "publish": None,
                          "top": False, "contentFormat": None,
                          "tagList": [{"id": 26, "name": "Java集合", "type": 0},
                                      {"id": 7, "name": "Java", "type": 0}]}]}
        return self.get_paginated_response(data)

    def retrieve(self, request, *args, **kwargs):
        id = kwargs['pk']
        instance = Article.objects.filter(id=id).first()
        # 阅读数加一
        Article.objects.filter(id=id).update(read_num=F('read_num') + 1)
        return Response({"id": instance.id, "createTime": instance.create_time, "updateTime": instance.update_time,
                         "title": instance.title, "description": instance.description, 'content': instance.content,
                         "read_num": instance.read_num, "like_num": instance.like_num, "cover": instance.cover,
                         "cover_type": instance.cover_type, 'top': instance.top,
                         'content_format': instance.content_format,
                         "tags": [{'id': i.id, 'name': i.name} for i in instance.tags]})

    @action(methods=['POST'], url_path='like', detail=True)
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
