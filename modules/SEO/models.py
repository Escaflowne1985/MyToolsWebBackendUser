from dvadmin.system.models import *


class SEOManage(CoreModel):
    site = models.CharField(max_length=255, verbose_name="站点名称", null=True, blank=True)
    category = models.CharField(max_length=255, verbose_name="分类", null=True, blank=True)
    item = models.CharField(max_length=255, verbose_name="栏目", null=True, blank=True)
    modules = models.CharField(max_length=255, verbose_name="模板名称", null=True, blank=True)
    id_image = models.CharField(max_length=255, verbose_name="封面id", null=True, blank=True)
    name = models.CharField(max_length=255, verbose_name="标签名称", null=True, blank=True)
    slug = models.CharField(max_length=255, verbose_name="唯一标识", null=True, blank=True)

    class Meta:
        verbose_name = "SEO站点分类"
        verbose_name_plural = verbose_name


class SEOModules(CoreModel):
    name = models.CharField(max_length=255, verbose_name="模版名称", null=True, blank=True)
    content = models.TextField(verbose_name="提问方式", null=True, blank=True)
    explain = models.TextField(verbose_name="解释说明", null=True, blank=True)

    class Meta:
        verbose_name = "SEO提问方式"
        verbose_name_plural = verbose_name
