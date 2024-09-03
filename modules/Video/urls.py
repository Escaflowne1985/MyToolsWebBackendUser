# -*- coding: UTF-8 -*-

from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import *

router = DefaultRouter()
router.register('SrtSubTitle', SrtSubTitleViewSet, 'SrtSubTitle')
router.register('VideoClipMixingCut', VideoClipMixingCutViewSet, 'VideoClipMixingCut')



urlpatterns = [
    path('VideoClipMixingCut_task/', VideoClipMixingCut_task, name='VideoClipMixingCut_task'),
]
urlpatterns += router.urls
