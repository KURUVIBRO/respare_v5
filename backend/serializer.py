from rest_framework import serializers
from backend.models import Choice
class ChoiceIdSerializer(serializers.Serializer):
    id=serializers.IntegerField()

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Choice
        fields=['id','option','count']