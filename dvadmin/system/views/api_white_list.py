# -*- coding: utf-8 -*-

"""
@Remark:白名单
"""
from dvadmin.system.models import ApiWhiteList
from dvadmin.utils.serializers import CustomModelSerializer
from dvadmin.utils.viewset import CustomModelViewSet


class ApiWhiteListSerializer(CustomModelSerializer):
    """
    接口白名单-序列化器
    """

    class Meta:
        model = ApiWhiteList
        fields = "__all__"
        read_only_fields = ["id"]





class ApiWhiteListViewSet(CustomModelViewSet):
    """
    接口白名单
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = ApiWhiteList.objects.all()
    serializer_class = ApiWhiteListSerializer
    # permission_classes = []
