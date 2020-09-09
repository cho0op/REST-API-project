from status.models import Status
from rest_framework import serializers


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            'id',
            'user',
            'content',
            'image',
        ]
        read_only_fields = ['user']

    def validate(self, attrs):
        content = attrs.get('content', None)
        image = attrs.get('image', None)
        if content == "":
            content = None
        if content is None and image is None:
            raise serializers.ValidationError("img or content is required")
        print(attrs)
        return attrs
