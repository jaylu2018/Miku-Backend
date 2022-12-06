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

    def list(self, request, *args, **kwargs):
        data = super().list(request, *args, **kwargs)
        # data = [
        #     {
        #         "id": "0",
        #         "deptName": "华东分部",
        #         "orderNo": 1,
        #         "createTime": "2019-10-10 15:45:46",
        #         "remark": "阶定圆说属流变总布好月例合器科料场来",
        #         "status": "0",
        #         "children": [
        #             {
        #                 "id": "0-0",
        #                 "deptName": "研发部",
        #                 "orderNo": 1,
        #                 "createTime": "2012-06-21 11:15:10",
        #                 "remark": "先质四保以带候使联切米后装多机真",
        #                 "status": "1",
        #                 "parentDept": "0"
        #             },
        #             {
        #                 "id": "0-1",
        #                 "deptName": "市场部",
        #                 "orderNo": 2,
        #                 "createTime": "2018-12-06 06:54:30",
        #                 "remark": "做之共话看般变它南备算光指",
        #                 "status": "1",
        #                 "parentDept": "0"
        #             },
        #             {
        #                 "id": "0-2",
        #                 "deptName": "商务部",
        #                 "orderNo": 3,
        #                 "createTime": "1985-11-13 03:50:39",
        #                 "remark": "亲转新选文易样空力了带委规可重证不",
        #                 "status": "0",
        #                 "parentDept": "0"
        #             },
        #             {
        #                 "id": "0-3",
        #                 "deptName": "财务部",
        #                 "orderNo": 4,
        #                 "createTime": "1977-08-07 19:54:41",
        #                 "remark": "道办话角易劳合运了开边色",
        #                 "status": "0",
        #                 "parentDept": "0"
        #             }
        #         ]
        #     },
        #     {
        #         "id": "1",
        #         "deptName": "华南分部",
        #         "orderNo": 2,
        #         "createTime": "2006-08-14 00:25:08",
        #         "remark": "教置采号需百日间运毛江门车西及",
        #         "status": "1",
        #         "children": [
        #             {
        #                 "id": "1-0",
        #                 "deptName": "研发部",
        #                 "orderNo": 1,
        #                 "createTime": "2016-02-17 11:11:20",
        #                 "remark": "转道较二组青提起算眼置验化质意么是",
        #                 "status": "1",
        #                 "parentDept": "1"
        #             },
        #             {
        #                 "id": "1-1",
        #                 "deptName": "市场部",
        #                 "orderNo": 2,
        #                 "createTime": "2021-11-24 16:18:48",
        #                 "remark": "众成用写共马放个非术度办叫少而入府毛式",
        #                 "status": "0",
        #                 "parentDept": "1"
        #             },
        #             {
        #                 "id": "1-2",
        #                 "deptName": "商务部",
        #                 "orderNo": 3,
        #                 "createTime": "2002-10-19 10:23:36",
        #                 "remark": "成同易时议复道是造标解",
        #                 "status": "1",
        #                 "parentDept": "1"
        #             },
        #             {
        #                 "id": "1-3",
        #                 "deptName": "财务部",
        #                 "orderNo": 4,
        #                 "createTime": "2006-03-05 05:56:30",
        #                 "remark": "去利越时和工列决开般",
        #                 "status": "0",
        #                 "parentDept": "1"
        #             }
        #         ]
        #     },
        #     {
        #         "id": "2",
        #         "deptName": "西北分部",
        #         "orderNo": 3,
        #         "createTime": "1988-03-16 09:35:07",
        #         "remark": "越引子已记状适调可料证且电向",
        #         "status": "0",
        #         "children": [
        #             {
        #                 "id": "2-0",
        #                 "deptName": "研发部",
        #                 "orderNo": 1,
        #                 "createTime": "2015-06-20 01:35:35",
        #                 "remark": "些圆率众级完查克支与经边于",
        #                 "status": "0",
        #                 "parentDept": "2"
        #             },
        #             {
        #                 "id": "2-1",
        #                 "deptName": "市场部",
        #                 "orderNo": 2,
        #                 "createTime": "1982-06-19 17:10:37",
        #                 "remark": "能把具验龙几心北据历年",
        #                 "status": "1",
        #                 "parentDept": "2"
        #             },
        #             {
        #                 "id": "2-2",
        #                 "deptName": "商务部",
        #                 "orderNo": 3,
        #                 "createTime": "2013-10-06 22:30:34",
        #                 "remark": "群论第表信七属想始单象整接确西他化西",
        #                 "status": "1",
        #                 "parentDept": "2"
        #             },
        #             {
        #                 "id": "2-3",
        #                 "deptName": "财务部",
        #                 "orderNo": 4,
        #                 "createTime": "2005-03-31 10:16:05",
        #                 "remark": "并走主又它行西四半里内同设和位比大",
        #                 "status": "0",
        #                 "parentDept": "2"
        #             }
        #         ]
        #     }
        # ]
        return VbenResponse(data=data.data, msg='ok', code=0, status=status.HTTP_200_OK, type_res='success')

    def create(self, request, *args, **kwargs):
        data = super().create(request, *args, **kwargs)
        return VbenResponse(data=data.data, msg='ok', code=0, status=status.HTTP_201_CREATED, type_res='success')

    def update(self, request, *args, **kwargs):
        data = super().update(request, *args, **kwargs)
        return VbenResponse(data=data.data, msg='ok', code=0, status=status.HTTP_200_OK, type_res='success')

    def destroy(self, request, *args, **kwargs):
        data = super().destroy(request, *args, **kwargs)
        return VbenResponse(data=data.data, msg='ok', code=0, status=status.HTTP_200_OK, type_res='success')
