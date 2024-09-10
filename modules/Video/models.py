from dvadmin.system.models import *


class VideoIntroductionClipCutData(CoreModel):
    level = models.TextField(verbose_name="层级", null=True, blank=True)
    task_name = models.CharField(max_length=255, verbose_name="任务名称", null=True, blank=True)
    task_id = models.CharField(max_length=30, verbose_name="任务ID", null=True, blank=True)
    name = models.CharField(max_length=255, verbose_name="目录名称", null=True, blank=True)
    txt = models.TextField(verbose_name="解说文案", null=True, blank=True)
    tag = models.CharField(max_length=30, verbose_name="序号任务", null=True, blank=True)

    class Meta:
        verbose_name = "视频介绍应用"
        verbose_name_plural = verbose_name
