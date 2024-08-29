# -*- coding: UTF-8 -*-

from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import *

router = DefaultRouter()

router.register('AudioFunAsr', AudioFunAsrViewSet, 'AudioFunAsr')
# router.register('AudioWhisper', AudioWhisperViewSet, 'AudioWhisper')
router.register('AudioFasterWhisper', AudioFasterWhisperViewSet, 'AudioFasterWhisper')

urlpatterns = [
    path('funasr_task/', funasr_task, name='funasr_task'),
    # path('whisper_task/', whisper_task, name='whisper_task'),
    path('fasterwhisper_task/', fasterwhisper_task, name='fasterwhisper_task'),

]
urlpatterns += router.urls
