# env setup.py/py
# -*- coding: UTF-8 -*-

from django_filters import rest_framework as filters
from modules.Video.models import *


class VideoIntroductionClipCutFilter(filters.FilterSet):
    class Meta:
        model = VideoIntroductionClipCutData
        fields = '__all__'


class VideoRepeatFunAsrFilter(filters.FilterSet):
    class Meta:
        model = VideoRepeatFunAsr
        fields = '__all__'


class VideoRepeatStoryFilter(filters.FilterSet):
    class Meta:
        model = VideoRepeatStory
        fields = '__all__'


class VideoCamSrtFilter(filters.FilterSet):
    class Meta:
        model = VideoCamSrt
        fields = '__all__'
