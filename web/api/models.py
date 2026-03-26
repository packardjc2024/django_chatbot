from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField



class Credential(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    password = models.CharField(max_length=255)
    application = models.CharField(max_length=255)

    class Meta:
        unique_together = ('user', 'application')