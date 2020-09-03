from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins

from status.models import Status
from status.api.serializers import StatusSerializer

import json


class StatusAPIView(generics.ListAPIView,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
    authentication_classes = []
    permission_classes = []
    serializer_class = StatusSerializer

    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def get_object(self):
        request = self.request
        passed_id = request.GET.get("id", None)
        queryset = self.get_queryset()
        obj = None
        if passed_id is not None:
            obj = get_object_or_404(queryset, id=passed_id)
            self.check_object_permissions(request, obj)
        return obj

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        passed_id = request.GET.get("id", None)
        if passed_id is not None:
            return self.retrieve(request, *args, **kwargs)  # call get_object
        return super().get(self, request, *args, **kwargs)  # to save old get() method

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        passed_id = request.GET.get("id", None)
        if passed_id is not None:
            return self.destroy(request, *args, **kwargs)  
        return super().get(self, request, *args, **kwargs)


class StatusCreateAPIView(generics.CreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = StatusSerializer
    queryset = Status.objects.all()


class StatusDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
    lookup_field = "id"  # or use 'pk' in url path

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class StatusUpdateAPIView(generics.UpdateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = StatusSerializer
    queryset = Status.objects.all()


class StatusDeleteAPIView(generics.DestroyAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = StatusSerializer
    queryset = Status.objects.all()


class StatusListSearchAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)
        return Response(serializer.data)
