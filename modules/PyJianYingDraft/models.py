from django.db import models
from dvadmin.utils.models import CoreModel, SoftDeleteModel


# Create your models here.


class AIStoryboardTextRenderer(CoreModel, SoftDeleteModel):
    task_id = models.CharField(max_length=255, verbose_name="任务id", blank=True, null=True)
    order_id = models.CharField(max_length=255, verbose_name="序号", blank=True, null=True)
    level = models.CharField(max_length=255, verbose_name="层级", blank=True, null=True)
    srt_text = models.TextField(verbose_name="文案信息", blank=True, null=True)
    audio = models.TextField(verbose_name="音频地址", blank=True, null=True)
    audio_duration = models.CharField(max_length=255, verbose_name="音频时长", blank=True, null=True)
    key_frame = models.CharField(max_length=255, verbose_name="关键帧方向", blank=True, null=True)
    style = models.CharField(max_length=255, verbose_name="风格标签", blank=True, null=True)
    role_name = models.JSONField(verbose_name="角色名称", blank=True, null=True)
    role_path = models.CharField(max_length=100, verbose_name="角色LoRA路径", blank=True, null=True)
    prompt_en = models.TextField(verbose_name="关键词描述(英文)", blank=True, null=True)
    prompt_zh = models.TextField(verbose_name="关键词描述(中文)", blank=True, null=True)
    image_select = models.TextField(verbose_name="选择图片地址", blank=True, null=True)
    image_list = models.TextField(verbose_name="选择图片地址列表", blank=True, null=True)
    api_task_id = models.CharField(max_length=255, verbose_name="API请求使用的task id", blank=True, null=True)

    class Meta:
        verbose_name = "文生视频原创"
        verbose_name_plural = verbose_name
