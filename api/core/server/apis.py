# coding: utf-8
from django.core.exceptions import ValidationError as DjangoValidationError
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException, ValidationError as RestValidationError
from rest_framework import status


class ValidationError(Exception):
    u"""
    API 基础验证异常
    """
    status_code = status.HTTP_400_BAD_REQUEST
    errors = {}  # 子项目需要对这个字典赋值

    def __init__(self, code, status_code=None, data=None, errormsg=None):
        if isinstance(code, int):
            self.code = code
            self.message = self.errors.get(code) if not errormsg else errormsg
        else:
            self.code = code.code
            self.message = code.message

        self.data = data
        if status_code is not None:
            self.status_code = status_code
        super(ValidationError, self).__init__(self.message)


def api_exception_handler(exc, context):
    u"""
    通用异常处理
    """
    if isinstance(exc, ValidationError):
        response = Response({})
        response.data['result'] = False
        response.data['errormsg'] = exc.message
        response.data['resultcode'] = exc.code
        response.data['data'] = exc.data
        return response
    elif isinstance(exc, DjangoValidationError):
        response = Response({})
        response.data['result'] = False
        response.data['errormsg'] = exc.message
        response.data['resultcode'] = exc.code
        if isinstance(exc.error_list, list):
            response.data['data'] = ' '.join(
                [e for e in exc.error_list]) if exc.error_list else ''
        else:
            response.data['data'] = exc.error_list
        return response
    elif isinstance(exc, RestValidationError):
        response = Response({})
        response.data['result'] = False
        if isinstance(exc.detail, list):
            errormsgs = []
            for detail in exc.detail:
                if isinstance(detail, dict):
                    errormsgs.append(' '.join(
                        ['{}: {}'.format(k, ' '.join(v) if isinstance(v, list) else v)
                         for k, v in detail.iteritems()]))
                else:
                    errormsgs.append(detail)
            response.data['errormsg'] = ' '.join(errormsgs)
        elif isinstance(exc.detail, dict):
            response.data['errormsg'] = ' '.join(
                ['{}: {}'.format(k, ' '.join(v) if isinstance(v, list) else v)
                 for k, v in exc.detail.iteritems()])
        else:
            response.data['errormsg'] = exc.detail
        response.data['resultcode'] = exc.status_code
        return response
    elif isinstance(exc, APIException):
        response = Response({}, exc.status_code in (
            401, 403) and 200 or exc.status_code)
        response.data['result'] = False
        response.data['errormsg'] = exc.detail
        response.data['resultcode'] = exc.status_code
        return response
    elif isinstance(exc, Http404):
        response = Response({}, 200)
        response.data['result'] = False
        response.data['errormsg'] = '无访问权限或数据已被删除'
        response.data['resultcode'] = 404
        return response
    return exception_handler(exc, context)


class CodeType(type):
    def __new__(cls, name, bases, attrs):
        attrs_value = {}
        ERROR = {}
        for k, v in attrs.items():
            if k.startswith('__'):
                continue
            if isinstance(v, (tuple, list)) and len(v) == 2:
                code, error_msg = v
                attrs_value[k] = ValidationError(code=code, errormsg=error_msg)
                ERROR[code] = error_msg
            else:
                attrs_value[k] = v

        obj = type.__new__(cls, name, bases, attrs_value)
        ValidationError.errors.update(ERROR)
        return obj


class APICode(object):
    __metaclass__ = CodeType

    unauthorized = (401, '未认证')
    forbidden = (403, '无权限')
    notfound = (404, '数据不存在')
