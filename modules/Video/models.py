from dvadmin.system.models import *


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
