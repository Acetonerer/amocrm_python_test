from django.db import models
from incident.managers import IncidentManager


class Incident(models.Model):
    incident_id = models.AutoField(primary_key=True)
    machine_ip = models.CharField(max_length=100, db_index=True)
    type_of_parameter = models.CharField(max_length=10)
    value_of_parameter = models.CharField(max_length=10)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now=True, db_index=True)

    objects = IncidentManager()

    class Meta:
        db_table = "incident_storage"
        