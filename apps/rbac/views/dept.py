from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from apps.rbac.models.dept import Dept
from apps.rbac.serializers.dept import DeptSerializer
from utils.responses.base_response import VbenResponse


class DeptViewSet(ModelViewSet):
    """
    部门管理：增删改查
    """
    serializer_class = DeptSerializer
    queryset = Dept.objects.all().order_by('-update_time')  # 按时间倒序

    # def delete_children_is_null(self, data):
    #     """递归删除children为空的数据"""
    #     for item in data:
    #         if item['children']:
    #             self.delete_children_is_null(item['children'])
    #         else:
    #             del item['children']
    #     return data

    def serialize_tree(self, queryset):
        for obj in queryset:
            data = self.get_serializer(obj).data
            data['children'] = self.serialize_tree(obj.children.all())
            yield data

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(parent=None)
        data = self.serialize_tree(queryset)
        # data = self.delete_children_is_null(data)
        return VbenResponse(data=data, msg='ok', code=0, status=status.HTTP_201_CREATED, type_res='success')

    # def list(self, request, *args, **kwargs):
    #     datas = super().list(request, *args, **kwargs).data
    #     # data = [item for item in datas if item['children']]
    #     # id_list = []
    #     # for item in datas:
    #     #     if not item['children']:
    #     #         item.pop('children')
    #     #     else:
    #     #         for child in item['children']:
    #     #             id_list.append(child['id'])
    #     # print(id_list)
    #     # for item in datas:
    #     #     print(item)
    #     #     if item['id'] in id_list:
    #     #         datas.remove(item)
    #     return VbenResponse(data=datas, msg='ok', code=0, status=status.HTTP_200_OK, type_res='success')

    def create(self, request, *args, **kwargs):
        data = super().create(request, *args, **kwargs)
        return VbenResponse(data=data.data, msg='ok', code=0, status=status.HTTP_201_CREATED, type_res='success')

    def update(self, request, *args, **kwargs):
        data = super().update(request, *args, **kwargs)
        return VbenResponse(data=data.data, msg='ok', code=0, status=status.HTTP_200_OK, type_res='success')

    def destroy(self, request, *args, **kwargs):
        data = super().destroy(request, *args, **kwargs)
        return VbenResponse(data=data.data, msg='ok', code=0, status=status.HTTP_200_OK, type_res='success')
