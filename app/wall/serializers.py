from rest_framework import serializers

from core.models import Wall


class WallSerializer(serializers.ModelSerializer):
    """Serializer for wall objects"""

    class Meta:
        model = Wall
        fields = ('id', 'title', 'body')
        read_only_fields = ('id',)
