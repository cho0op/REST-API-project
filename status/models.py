from django.db import models
from django.conf import settings


def upload_path(instance, filename):
    return f"status/{instance.user.username}/{filename}"


class StatusQuerySet(models.QuerySet):
    pass


class StatusManager(models.Manager):
    def get_queryset(self):
        return StatusQuerySet(self.model, using=self._db)


class Status(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to=upload_path)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = StatusManager

    class Meta:
        verbose_name = "status"
        verbose_name_plural = "statuses"
# Create your models here.
