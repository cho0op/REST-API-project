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
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    # def get(self, request, format=None):
    #     qs = Status.objects.all()
    #     serializer = StatusSerializer(qs, many=True)
    #     return Response(serializer.data)


class StatusCreateAPIView(generics.CreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = StatusSerializer
    queryset = Status.objects.all()


class StatusDetailAPIView(generics.RetrieveAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
    lookup_field = "id"  # or use 'pk' in url path


class StatusListSearchAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)
        return Response(serializer.data)
