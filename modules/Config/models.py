from django.db import models


# Create your models here.


class Configuration(models.Model):
    model_name = models.CharField(max_length=255, unique=True)
    parameters = models.JSONField()

    def __str__(self):
        return self.model_name
