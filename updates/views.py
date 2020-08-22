from django.shortcuts import render
from django.http import JsonResponse


def update_detail_json_view(request):
    data = {
        "amount": 3,
        "type": "update"
    }
    return JsonResponse(data=data)

# Create your views here.
