# -*- coding: utf-8 -*-

from modules.Video.models import *
from dvadmin.utils.serializers import *


class VideoIntroductionClipCutSerializer(CustomModelSerializer):
    class Meta:
        model = VideoIntroductionClipCutData
        fields = '__all__'


class VideoRepeatFunAsrSerializer(CustomModelSerializer):
    class Meta:
        model = VideoRepeatFunAsr
        fields = '__all__'


class VideoRepeatStorySerializer(CustomModelSerializer):
    class Meta:
        model = VideoRepeatStory
        fields = '__all__'


class VideoCamSrtSerializer(CustomModelSerializer):
    class Meta:
        model = VideoCamSrt
        fields = '__all__'
