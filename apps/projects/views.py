import logging

from django.db.models import Count
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, status

from utils.responses.base_response import APIResponse
from .models import Projects
from .serializers import ProjectsModelSerializer, ProjectsNamesModelSerializer, \
    InterfacesNamesModelSerializer, InterfacesByProjectsIdModelSerializer

# 定义日志器用于记录日志，logging.getLogger('全局配置settings.py中定义的日志器名')
# logger = logging.getLogger('mytest')
from ..interfaces.models import Interfaces
from ..suits.models import Testsuits


class ProjectsViewSet(ModelViewSet):
    queryset = Projects.objects.all().order_by("id")
    serializer_class = ProjectsModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def list(self, request, *args, **kwargs):
    #     datas = super().list(request, *args, **kwargs)
    #     data = {
    #         "page": datas.data['current_page_num'],
    #         "pageSize": 10,
    #         "pageCount": datas.data['total_pages'],
    #         "itemCount": datas.data['count'],
    #         "list": datas.data['results']
    #     }
    #     for i in datas.data['results']:
    #         # 需要获取当前项目所属的接口总数、用例总数、配置总数、套件总数
    #         project_id = i.get('id')
    #         qs = Interfaces.objects.values('id').annotate(testcases=Count('testcases')).filter(project_id=project_id)
    #         # 接口总数
    #         interfaces_count = qs.count()
    #
    #         # 案例总数
    #         testcases_count = 0
    #         for one_dict in qs:
    #             testcases_count += one_dict.get('testcases')
    #
    #         # 套件总数
    #         testsuites_count = Testsuits.objects.filter(project_id=project_id).count()
    #
    #         # 获取项目下的配置总数
    #         qs = Interfaces.objects.values('id').annotate(configs=Count('configs')).filter(project_id=project_id)
    #         configs_count = 0
    #         for one_dict in qs:
    #             configs_count += one_dict.get('configs')
    #         i['testcases_count'] = testcases_count
    #         i['interfaces_count'] = interfaces_count
    #         i['testsuites_count'] = testsuites_count
    #         i['configs_count'] = configs_count
    #     return APIResponse(data=data, msg='ok', code=200, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = response.data['results']
        return APIResponse(data=response.data, msg='ok', code=200, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return APIResponse(data=response.data, msg='ok', code=200, status=status.HTTP_201_CREATED)

    @action(detail=False)
    def names(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @action(detail=True)
    def interfaces(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
        # instance = self.get_object()
        # # qs = Interfaces.objects.filter(projects=instance)
        # serializer_obj = self.get_serializer(instance=instance)
        # # 进行过滤和分页操作
        # return Response(serializer_obj.data)
        # return self.retrieve(request, *args, **kwargs)
        # response = self.retrieve(request, *args, **kwargs)
        # response.data = response.data['interfaces']
        # return response

    def get_serializer_class(self):
        if self.action == 'names':
            return ProjectsNamesModelSerializer
        elif self.action == 'interfaces':
            return InterfacesByProjectsIdModelSerializer
        else:
            return self.serializer_class
