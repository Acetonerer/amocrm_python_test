from django.db import models
from collections import deque


class MetricStorageManager(models.Manager):

    def check_threshold(self, machine_ip, field_name, threshold, n):
        """
        Проверяет, превышает ли среднее значение указанного поля заданный порог
        для последних n записей, связанных с машиной по IP-адресу.
        """

        records = self.filter(machine_ip=machine_ip).order_by('-created_at')[:n]
        total_value = 0

        for record in records:
            field_value = getattr(record, field_name, None)

            if field_value is None:
                return False

            if isinstance(field_value, str) and '%' in field_value:
                field_value = field_value.replace('%', '')
            try:
                field_value = float(field_value)
            except ValueError:
                return False

            total_value += field_value
        average_value = round(total_value / n, 2)
        exceeded = average_value > threshold
        return exceeded, average_value
