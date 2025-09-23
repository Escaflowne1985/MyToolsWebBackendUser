# coding:utf-8
'''
@IDE     ：PyCharm 
@Project ：MyAIToolsClient.py 
@File    ：apps.py.py
@Author  ：Mr数据杨
@Date    ：2025/9/11
@Desc    : 
'''

# coding: utf-8
from django.apps import AppConfig


class ScriptConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    # 使用“完整的 Python 路径”指向此包
    name = "modules.script"
    # 可自定义 label，避免与别的 app label 冲突
    label = "script"

