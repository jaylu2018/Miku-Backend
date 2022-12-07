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

    def delete_bad_key(self, badKey, dictionary):
        for key in list(dictionary.keys()):
            if key == badKey and dictionary[key] == []:
                del dictionary[key]
            elif type(dictionary[key]) == dict:
                self.delete_bad_key(badKey, dictionary[key])
            elif type(dictionary[key]) == list:
                for item in dictionary[key]:
                    self.delete_bad_key(badKey, item)
        return dictionary

    def serialize_tree(self, queryset):
        data = []
        for obj in queryset:
            datas = self.get_serializer(obj).data
            datas['children'] = self.serialize_tree(obj.children.all())
            data.append(datas)
        return data

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(parent=None)
        data_list = self.serialize_tree(queryset)
        datas = [self.delete_bad_key('children', data) for data in data_list]
        return VbenResponse(data=datas, msg='ok', code=0, status=status.HTTP_201_CREATED, type_res='success')

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
