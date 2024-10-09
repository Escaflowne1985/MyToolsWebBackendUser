# -*- coding: utf-8 -*-

from modules.SEO.models import *
from dvadmin.utils.serializers import *


class SEOManageSerializer(CustomModelSerializer):
    class Meta:
        model = SEOManage
        fields = '__all__'
