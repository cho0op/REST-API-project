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
        passed_id = json.loads(request.body).get("id")
        obj = get_object_or_404(Status, id=passed_id)
        self.check_object_permissions(request, obj)
        return obj

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


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
