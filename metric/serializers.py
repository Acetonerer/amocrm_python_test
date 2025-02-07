from rest_framework import serializers
from metric.models import MetricStorage


class MetricStorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetricStorage
        fields = ["machine_ip", "cpu", "mem", "disk", "uptime"]
