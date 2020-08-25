import json

from django.views import View
from django.http import HttpResponse

from updates.models import Update
from updates.forms import UpdateForm
from updates.api_tests.mixins import CSRFExemptMixin, HttpResponseMixin
from django.contrib.auth.models import User


class UpdateListAPIView(HttpResponseMixin, CSRFExemptMixin, View):
    def get(self, request, **kwargs):
        qs = Update.objects.all()
        json_data = qs.serialize()
        return self.render_response(data=json_data)

    def post(self, request, *args, **kwargs):
        data = {
            "message": "post method"
        }
        update_form = UpdateForm(request.POST)
        if update_form.is_valid():
            update_obj = update_form.save()
            json_data = update_obj.serialize()
            return self.render_response(data=json_data, status=400)
        if update_form.errors:
            data = json.dumps(update_form.errors)
            return self.render_response(data, status=403)

    def delete(self, *args, **kwargs):
        data = {
            "message": "delete method"
        }
        json_data = json.dumps(data)
        return self.render_response(data=json_data, status=403)


class UpdateDetailAPIView(HttpResponseMixin, CSRFExemptMixin, View):
    def get(self, request, update_id, *args, **kwargs):
        obj = Update.objects.get(id=update_id)
        json_data = obj.serialize()
        return self.render_response(data=json_data)
