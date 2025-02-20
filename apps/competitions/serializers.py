from rest_framework import serializers
from apps.competitions.models import *


class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = [
            'badge_id','name', 'image', 'created_by', 'created_at', 'imagePath'
        ]


