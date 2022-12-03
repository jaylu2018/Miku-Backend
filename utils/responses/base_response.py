from rest_framework import serializers
from rest_framework.response import Response


class APIResponse(Response):
    """
    自定义接口响应数据格式类
    1.在视图类中的APIView中使用该JsonResponse返回响应数据
    2.ModelViewSet、Mixin下派生的APIView类、views.APIView都需要自己重写并返回JsonResponse格式的数据
    """

    def __init__(self, data=None, code=None, msg=None, status=None, template_name=None,
                 headers=None, exception=False, content_type=None):
        super().__init__(None, status=status)

        if isinstance(data, serializers.Serializer):
            msg = (
                'You passed a Serializer instance as data, but '
                'probably meant to pass serialized `.data` or '
                '`.error`. representation.'
            )
            raise AssertionError(msg)
        self.data = {
            'code': code,
            'msg': msg,
            'data': data,
        }
        self.template_name = template_name
        self.exception = exception
        self.content_type = content_type

        if headers:
            for name, value in headers.items():
                self[name] = value


class NaiveResponse(Response):
    def __init__(self, data=None, code=None, msg=None, status=None, template_name=None,
                 headers=None, exception=False, content_type=None):
        super().__init__(None, status=None)
        if isinstance(data, serializers.Serializer):
            msg = (
                'You passed a Serializer instance as data, but '
                'probably meant to pass serialized `.data` or '
                '`.error`. representation.'
            )
            raise AssertionError(msg)
        self.data = {
            'code': code,
            'msg': msg,
            'data': data,
        }
        self.template_name = template_name
        self.exception = exception
        self.content_type = content_type

        if headers:
            for name, value in headers.items():
                self[name] = value


class VbenResponse(Response):
    def __init__(self, data=None, code=None, msg=None, status=None, type_res=None, template_name=None,
                 headers=None, exception=False, content_type=None):
        super().__init__(None, status=None)
        if isinstance(data, serializers.Serializer):
            msg = (
                'You passed a Serializer instance as data, but '
                'probably meant to pass serialized `.data` or '
                '`.error`. representation.'
            )
            raise AssertionError(msg)
        self.data = {
            'code': code,
            'message': msg,
            'result': data,
            'type': type_res
        }
        self.template_name = template_name
        self.exception = exception
        self.content_type = content_type

        if headers:
            for name, value in headers.items():
                self[name] = value
