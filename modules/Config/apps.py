from django.apps import AppConfig


class ConfigConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'modules.Config'
    label = "config"  # 供 apps.get_model("Config","Configuration") 使用
