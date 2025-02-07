from rest_framework import serializers
from incident.models import Incident


class IncidentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Incident
    """
    class Meta:
        model = Incident
        fields = "__all__"
