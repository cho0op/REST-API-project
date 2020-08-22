import json

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from django.core.serializers import serialize

from .models import Update


def update_detail_json_view(request):
    data = {
        "amount": 3,
        "type": "update"
    }
    return JsonResponse(data=data)


class JsonResponseExample(View):
    def get(self, request, *args, **kwargs):
        data = {
            "amount": 3,
            "type": "update"
        }
        return JsonResponse(data=data)


class UpdateDetailView(View):
    def get(self, request, **kwargs):
        obj = Update.objects.get(id=1)
        json_data = obj.serialize()
        print(json_data)
        return HttpResponse(json_data, content_type="application/json")
        # data = {
        #     "content": obj.content,
        #     "username": obj.user
        # }
        # json_data = json.dumps(data)
        # return HttpResponse(json_data, content_type="application/json")


class UpdateListView(View):
    def get(self, request, **kwargs):
        json_data = Update.objects.all().serialize()
        print(json_data)
        return HttpResponse(json_data, content_type="application/json")
        # return JsonResponse(data, safe=False)
