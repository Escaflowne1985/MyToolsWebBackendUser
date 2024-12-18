# env setup.py/py
# -*- coding: UTF-8 -*-

from django_filters import rest_framework as filters
from modules.SEO.models import *


class SEOManageFilter(filters.FilterSet):
    class Meta:
        model = SEOManage
        fields = '__all__'

