import json

from django.views import View
from django.http import HttpResponse

from updates.models import Update
from updates.forms import UpdateForm
from updates.api_tests.mixins import CSRFExemptMixin, HttpResponseMixin
from .utils import is_json


class UpdateListAPIView(HttpResponseMixin, CSRFExemptMixin, View):
    def get(self, request, **kwargs):
        qs = Update.objects.all()
        json_data = qs.serialize()
        return self.render_response(data=json_data)

    def post(self, request, *args, **kwargs):
        data = {
            "message": "post method"
        }
        if not is_json(request.body.decode()):
            data = json.dumps({"message": "invalid data, please send JSON"})
            return self.render_response(data, status=400)
        data = json.loads(request.body.decode())
        update_form = UpdateForm(data)
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
    def get_object(self, _id):
        qs = Update.objects.filter(id=_id)
        if qs.count() == 1:
            return qs.first()
        return None

    def get(self, request, update_id, *args, **kwargs):
        obj = Update.objects.get(id=update_id)
        json_data = obj.serialize()
        return self.render_response(data=json_data)

    def put(self, request, update_id, *args, **kwargs):
        obj = self.get_object(update_id)
        print(request.body.decode())  # A request.body is data sent by the client to your API
        if not is_json(request.body.decode()):  # .decode because request.body is bytes type
            data = json.dumps({"message": "invalid data, please send JSON"})
            return self.render_response(data, status=400)
        json_data = json.dumps({"message": "put method"})
        return self.render_response(json_data)

    def delete(self, request, update_id, *args, **kwargs):
        obj = self.get_object(update_id)
        if obj is None:
            json_data = json.dumps({"message": f"there is no update with id {update_id}"})
            return self.render_response(json_data, status=404)
        obj.delete()
        data = {
            "message": f"object with id {update_id} was deleted"
        }
        json_data = json.dumps(data)
        return self.render_response(json_data)
