import json

from django.core.serializers import serialize
from django.db import models
from django.conf import settings


def upload_path(instance, filename):
    return f"updates/{instance.user}/{filename}"


class UpdateQuerySet(models.QuerySet):
    def serialize(self):
        values_list = list((self.values("user", 'content', 'img', 'id')))
        return json.dumps(values_list)


class UpdateManager(models.Manager):
    def get_queryset(self):
        return UpdateQuerySet(self.model, using=self._db)

    # def serialize(self):
    #     return self.get_queryset().serialize()


class Update(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    img = models.ImageField(blank=True, null=True, upload_to=upload_path)
    content = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = UpdateManager()

    def __str__(self):
        return self.content or ""

    def serialize(self):
        try:
            img_path = self.img.path
        except ValueError:
            img_path = "NO_IMAGE"
        print(img_path)
        data = {
            "id": self.id,
            "user": self.user.username,
            "content": self.content,
            "img": img_path,
        }
        return json.dumps(data)
# Create your models here.
