from django.db import models
from dvadmin.utils.models import CoreModel, SoftDeleteModel


class VideoIntroductionClipCutData(CoreModel):
    level = models.TextField(verbose_name="层级", null=True, blank=True)
    task_name = models.CharField(max_length=255, verbose_name="任务名称", null=True, blank=True)
    task_id = models.CharField(max_length=30, verbose_name="任务ID", null=True, blank=True)
    name = models.CharField(max_length=255, verbose_name="目录名称", null=True, blank=True)
    order_id = models.CharField(max_length=30, verbose_name="序号任务", null=True, blank=True)
    video_path = models.CharField(max_length=255, verbose_name="视频路径", null=True, blank=True)
    start_time = models.CharField(max_length=100, verbose_name="开始时间", null=True, blank=True)
    end_time = models.CharField(max_length=100, verbose_name="结束时间", null=True, blank=True)
    srt_text = models.TextField(verbose_name="解说文案", null=True, blank=True)
    txt = models.TextField(verbose_name="解说文案", null=True, blank=True)
    tag = models.CharField(max_length=30, verbose_name="序号任务", null=True, blank=True)

    class Meta:
        verbose_name = "视频介绍应用"
        verbose_name_plural = verbose_name


class VideoRepeatFunAsr(CoreModel):
    level = models.TextField(verbose_name="层级", null=True, blank=True)
    task_name = models.CharField(max_length=255, verbose_name="任务名称", null=True, blank=True)
    task_id = models.CharField(max_length=30, verbose_name="任务ID", null=True, blank=True)
    order_id = models.IntegerField(verbose_name="任务数据序号", null=True, blank=True)
    status_use = models.BooleanField(verbose_name="是否使用", default=1, null=True, blank=True)
    status_rewrite = models.BooleanField(verbose_name="是否洗稿", default=1, null=True, blank=True)
    speaker = models.CharField(max_length=30, verbose_name="说话人", null=True, blank=True)
    start_time = models.CharField(max_length=100, verbose_name="开始时间", null=True, blank=True)
    end_time = models.CharField(max_length=100, verbose_name="结束时间", null=True, blank=True)
    srt_text = models.CharField(max_length=255, verbose_name="字幕", null=True, blank=True)
    rewrite_text = models.CharField(max_length=255, verbose_name="修改文案", null=True, blank=True)

    class Meta:
        verbose_name = "短剧复述剧情+解说"
        verbose_name_plural = verbose_name


class VideoRepeatStory(CoreModel):
    level = models.TextField(verbose_name="层级", null=True, blank=True)
    task_name = models.CharField(max_length=255, verbose_name="任务名称", null=True, blank=True)
    task_id = models.CharField(max_length=30, verbose_name="任务ID", null=True, blank=True)
    order_id = models.IntegerField(verbose_name="任务数据序号", null=True, blank=True)
    status_use = models.BooleanField(verbose_name="是否使用", default=1, null=True, blank=True)
    status_rewrite = models.BooleanField(verbose_name="是否洗稿", default=1, null=True, blank=True)
    start_time = models.CharField(max_length=100, verbose_name="开始时间", null=True, blank=True)
    end_time = models.CharField(max_length=100, verbose_name="结束时间", null=True, blank=True)
    srt_text = models.CharField(max_length=255, verbose_name="字幕", null=True, blank=True)
    rewrite_text = models.CharField(max_length=255, verbose_name="修改文案", null=True, blank=True)

    class Meta:
        verbose_name = "短剧复述剧情+解说"
        verbose_name_plural = verbose_name


class VideoCamSrt(CoreModel):
    level = models.TextField(verbose_name="层级", null=True, blank=True)
    task_name = models.CharField(max_length=255, verbose_name="任务名称", null=True, blank=True)
    task_id = models.CharField(max_length=30, verbose_name="任务ID", null=True, blank=True)
    order_id = models.IntegerField(verbose_name="任务数据序号", null=True, blank=True)
    status_use = models.BooleanField(verbose_name="是否使用", default=True, null=True, blank=True)
    start_time = models.CharField(max_length=100, verbose_name="开始时间", null=True, blank=True)
    end_time = models.CharField(max_length=100, verbose_name="结束时间", null=True, blank=True)
    srt_text = models.CharField(max_length=255, verbose_name="字幕", null=True, blank=True)

    class Meta:
        verbose_name = "直播内容过滤"
        verbose_name_plural = verbose_name


class AIStoryboardRoleBaseInfo(CoreModel, SoftDeleteModel):
    name = models.CharField(max_length=255, verbose_name="名称", blank=True, null=True)
    other_names = models.CharField(max_length=255, verbose_name="别名", blank=True, null=True)
    prompt_en = models.TextField(verbose_name="关键描述(英文)", blank=True, null=True)
    prompt_zh = models.TextField(verbose_name="关键描述(中文)", blank=True, null=True)
    info = models.CharField(max_length=255, verbose_name="备注", blank=True, null=True)
    trigger_words = models.CharField(max_length=255, verbose_name="触发词", blank=True, null=True)
    url = models.CharField(max_length=255, verbose_name="角色LoRA连接", blank=True, null=True)
    type = models.CharField(max_length=255, verbose_name="LoRA类型", blank=True, null=True)
    cover = models.CharField(max_length=255, verbose_name="封面地址", blank=True, null=True)
    lora_path = models.CharField(max_length=255, verbose_name="LoRA路径", blank=True, null=True)

    class Meta:
        verbose_name = "文生视频_角色设置"
        verbose_name_plural = verbose_name


class AIStoryboardRole(CoreModel, SoftDeleteModel):
    cover = models.CharField(max_length=255, verbose_name="封面地址", blank=True, null=True)
    name = models.CharField(max_length=255, verbose_name="角色名称", blank=True, null=True)
    other_names = models.CharField(max_length=255, verbose_name="别名", blank=True, null=True)
    prompt_en = models.TextField(verbose_name="关键描述(英文)", blank=True, null=True)
    prompt_zh = models.TextField(verbose_name="关键描述(中文)", blank=True, null=True)
    lora_path = models.CharField(max_length=255, verbose_name="LoRA路径", blank=True, null=True)

    class Meta:
        verbose_name = "文生视频_角色设置"
        verbose_name_plural = verbose_name


class AIStoryboardTextRenderer(CoreModel, SoftDeleteModel):
    task_id = models.CharField(max_length=255, verbose_name="任务id", blank=True, null=True)
    order_id = models.CharField(max_length=255, verbose_name="序号", blank=True, null=True)
    level = models.CharField(max_length=255, verbose_name="层级", blank=True, null=True)
    srt_text = models.TextField(verbose_name="文案信息", blank=True, null=True)
    audio = models.TextField(verbose_name="音频地址", blank=True, null=True)
    key_frame = models.CharField(max_length=255, verbose_name="关键帧方向", blank=True, null=True)
    style = models.CharField(max_length=255, verbose_name="风格标签", blank=True, null=True)
    role_name = models.CharField(max_length=100, verbose_name="角色名称", blank=True, null=True)
    prompt_en = models.TextField(verbose_name="关键词描述(英文)", blank=True, null=True)
    prompt_zh = models.TextField(verbose_name="关键词描述(中文)", blank=True, null=True)
    image_select = models.TextField(verbose_name="选择图片地址", blank=True, null=True)
    image_list = models.TextField(verbose_name="选择图片地址列表", blank=True, null=True)

    class Meta:
        verbose_name = "文生视频原创"
        verbose_name_plural = verbose_name
