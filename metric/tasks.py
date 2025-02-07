from celery import shared_task
from metric.models import MetricStorage
import requests
from metric.serializers import MetricStorageSerializer


@shared_task
def get_and_save_metric():
    """
    Задача по сбору, валидации и сохранению метрик
    Выполняем валидацию полученных данных с сохранением корректных в список и далее в БД
    """
    try:
        response = requests.get("https://forsanya.onrender.com/metrics")
        response.raise_for_status()
        metrics_data = response.json()
        valid_metrics = []

        for metric in metrics_data:
            serializer = MetricStorageSerializer(data=metric)
            if serializer.is_valid():
                valid_metrics.append(MetricStorage(**serializer.validated_data))
            else:
                print(f"Ошибка валидации: {serializer.errors}")

        if valid_metrics:
            MetricStorage.objects.bulk_create(valid_metrics)
            print("Метрики зафиксированы")
    except requests.RequestException as error:
        print(f"Возник момент при попытке обратиться к эндпоинту."
              f"Вот текст: {error}")
