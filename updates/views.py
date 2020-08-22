from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View


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
