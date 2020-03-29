# coding: utf-8
from collections import OrderedDict
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination, _positive_int


class Pagination(LimitOffsetPagination):
    """
    自定义分页类
    """
    page_query_param = 'page'
    limit_query_param = 'limit'
    default_limit = 10
    max_limit = 100

    def get_limit(self, request):
        """
        获取请求中，每页多少行
        """
        if self.limit_query_param:
            try:
                limit = request.query_params.get(self.limit_query_param, None)
                if limit is None:
                    limit = request.POST.get(self.limit_query_param, None)

                if limit is None:
                    return self.default_limit

                return _positive_int(
                    limit,
                    strict=True,
                    cutoff=self.max_limit
                )
            except (KeyError, ValueError, TypeError):
                pass

        return self.default_limit

    def get_page(self, request):
        """
        获取请求中，当前第几页
        """
        try:
            page_number = request.query_params.get(self.page_query_param, None)
            if page_number is None:
                page_number = request.POST.get(self.page_query_param, None)

            if page_number is None:
                return 1

            page_number = _positive_int(page_number)
            # 页码，限制最小值为1
            if page_number < 1:
                page_number = 1

            return page_number
        except (KeyError, ValueError, TypeError):
            return 1

    def paginate_queryset(self, queryset, request, view=None):
        """
        分页逻辑
        :param queryset:
        :param request:
        :param view:
        :return:
        """
        self.limit = self.get_limit(request)
        if self.limit is None:
            return None

        self.page_number = self.get_page(request)
        # 允许直接设置count
        if getattr(self, 'count', 0) <= 0:
            self.count = self.get_count(queryset)

        # 当前页码修正
        total_page = (self.count + self.limit - 1) // self.limit
        offset = 0
        if self.page_number:
            # 页码，限制最大值
            if self.page_number > total_page:
                self.page_number = total_page or 1

            offset = (self.page_number - 1) * self.limit

        self.request = request
        if self.count > self.limit and self.template is not None:
            self.display_page_controls = True

        if self.count == 0 or offset > self.count:
            return []

        return list(queryset[offset:offset + self.limit])

    def get_paginated_response(self, data):
        """
        分页条返回内容
        :param data:
        :return:
        """
        return Response(OrderedDict([
            ('page', self.page_number),
            ('limit', self.limit),
            ('count', self.count),
            ('total_page', (self.count + self.limit - 1) // self.limit),
            ('list', data)
        ]))
