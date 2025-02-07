from django.db import models


class IncidentManager(models.Manager):
    def create_incident(self, machine_ip, type_of_parameter, value_of_parameter, message):
        """
        Создает запись об инциденте.
        """
        return self.create(
            machine_ip=machine_ip,
            type_of_parameter=type_of_parameter,
            value_of_parameter=str(value_of_parameter),
            message=message,
        )
