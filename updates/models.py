from django.db import models
from django.conf import settings


def upload_path(instance, filename):
    return f"updates/{instance.user}/{filename}"


class Update(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    img = models.ImageField(blank=True, null=True, upload_to=upload_path)
    content = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content or ""
# Create your models here.
