from celery import shared_task, chain, group
from metric.tasks import get_and_save_metric
from incident.tasks import check_cpu_and_mem, check_disk


@shared_task
def start_save_and_check_task():
    chain(get_and_save_metric.s(), group(check_cpu_and_mem.s(), check_disk.s())).apply_async()
