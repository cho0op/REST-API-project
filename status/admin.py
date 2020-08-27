from django.contrib import admin
from .models import Status
from .forms import StatusForm


class StatusAdmin(admin.ModelAdmin):
    form = StatusForm
    list_display = ['user', '__str__', 'image']

admin.site.register(Status, StatusAdmin)
# Register your models here.
