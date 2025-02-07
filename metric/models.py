from django.db import models
from metric.managers import MetricStorageManager


class MetricStorage(models.Model):
    metric_id = models.AutoField(primary_key=True)
    machine_ip = models.CharField(max_length=30, db_index=True)
    cpu = models.CharField(max_length=10)
    mem = models.CharField(max_length=10)
    disk = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    uptime = models.CharField(max_length=100)

    objects = MetricStorageManager()

    class Meta:
        db_table = "metric_storage"
