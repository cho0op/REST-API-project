from status.api.serializers import StatusSerializer
from status.models import Status

obj = Status.objects.first()
print(StatusSerializer(obj))
