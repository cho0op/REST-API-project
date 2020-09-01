from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from status.models import Status
from status.api.serializers import StatusSerializer


class StatusListAPIView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = StatusSerializer

    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get("q")
        qs = qs.filter(content__icontains=query)
        print(query)
        return qs

    # def get(self, request, format=None):
    #     qs = Status.objects.all()
    #     serializer = StatusSerializer(qs, many=True)
    #     return Response(serializer.data)


class StatusListSearchAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)
        return Response(serializer.data)
