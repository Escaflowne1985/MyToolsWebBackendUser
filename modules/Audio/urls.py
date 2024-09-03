# -*- coding: UTF-8 -*-

from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import *

router = DefaultRouter()

router.register('AudioFunAsr', AudioFunAsrViewSet, 'AudioFunAsr')
router.register('AudioWhisper', AudioWhisperViewSet, 'AudioWhisper')
router.register('AudioFasterWhisper', AudioFasterWhisperViewSet, 'AudioFasterWhisper')
router.register('AudioMicrosoftTTS', AudioMicrosoftTTSViewSet, 'AudioMicrosoftTTS')
router.register('AudioMoYinTTS', AudioMoYinTTSViewSet, 'AudioMoYinTTS')

urlpatterns = [
    path('FunAsr_task/', FunAsr_task, name='FunAsr_task'),
    path('Whisper_task/', Whisper_task, name='Whisper_task'),
    path('FasterWhisper_task/', FasterWhisper_task, name='FasterWhisper_task'),
    path('MicrosoftTTS_task/', MicrosoftTTS_task, name='MicrosoftTTS_task'),
    path('MoYinTTS_task/', MoYinTTS_task, name='MoYinTTS_task'),
]
urlpatterns += router.urls
