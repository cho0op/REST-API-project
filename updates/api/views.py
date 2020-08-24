import json

from django.views import View
from django.http import HttpResponse

from updates.models import Update
from updates.api_tests.mixins import CSRFExemptMixin


class UpdateListAPIView(CSRFExemptMixin, View):
    def get(self, request, **kwargs):
        qs = Update.objects.all().serialize()
        return HttpResponse(qs, content_type="application/json")


class UpdateDetailAPIView(CSRFExemptMixin, View):
    def get(self, request, _id, *args, **kwargs):
        obj = Update.objects.get(id=_id)
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type="application/json")

    def post(self, request, _id, *args, **kwargs):
        data = {
            "message": "ooops"
        }
        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type="application/json")
