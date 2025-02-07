from celery import shared_task
from metric.models import MetricStorage
from incident.models import Incident


@shared_task
def check_cpu_and_mem(*args, **kwargs):
    """
    Задача для проверки превышения средних значений
    cpu и mem за последние 30 минут
    """
    machines = MetricStorage.objects.values('machine_ip').distinct()

    for machine in machines:
        machine_ip = machine['machine_ip']

        cpu_exceeded, avg_cpu = MetricStorage.objects.check_threshold(machine_ip, 'cpu', 85, 3)
        if cpu_exceeded:
            Incident.objects.create_incident(
                machine_ip=machine_ip,
                type_of_parameter="CPU",
                value_of_parameter=avg_cpu,
                message=f"CPU usage more than 85% (actual: {avg_cpu}%) for 30 minutes"
            )

        mem_exceeded, avg_mem = MetricStorage.objects.check_threshold(machine_ip, 'mem', 90, 3)
        if mem_exceeded:
            Incident.objects.create_incident(
                machine_ip=machine_ip,
                type_of_parameter="Memory",
                value_of_parameter=avg_mem,
                message=f"Memory usage more than 90% (actual: {avg_mem}%) for 30 minutes"
            )
    print("Проверка цп и мемов завершена")


@shared_task
def check_disk(*args, **kwargs):
    """
    Проверка среднего значения Disk через алгоритм скользящего окна
    """
    machines = MetricStorage.objects.values('machine_ip').distinct()
    for machine in machines:
        machine_ip = machine['machine_ip']

        disk_exceeded, avg_disk = MetricStorage.objects.check_threshold(machine_ip, 'disk', 95, 9)
        if disk_exceeded:
            Incident.objects.create_incident(
                machine_ip=machine_ip,
                type_of_parameter='Disk',
                value_of_parameter=avg_disk,
                message=f"Disk usage more than 95% (actual: {avg_disk}%) for 2 hours "
            )
    print("Проверка нормального диска завершена")

