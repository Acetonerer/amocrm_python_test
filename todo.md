Общие пункты реализации по тестовому
1. Настроить проект, параметры бд для MySQL 8
2. Создать файл .env и вынести в него переменные
3. Описать модель метрик MetricStorage
4. Описать задачу Celery по обращению к внешнему эндпоинту
5. Описать модель инцидентов Incident
6. Реализовать сигнал на сохранение записи в MetricStorage. Отказ в пользу двух периодических задач
7. Протестировать весь функционал
8. Контейнеризировать
9. Залить на гит

10. Динамический пункт

Подробнее по каждому пункту

1: +
- Настройка параметров БД
- Настройка Celery/Redis
- 
2: +
- Создаём файл .env
- Вносим в него переменные окружения
- 
3: +
- Описываем модель MetricStorage
- Реализуем доп. поле machine_ip
- Через Class Meta задаём название таблице metric_storage
- Создаем миграции
- Выполняем

4: ++++
- Создаем файл celery.py в директории проекта
- Реализовать сериализатор для валидации данных
- Пишем задачу Celery для обращения к эндпоинту каждые 15 минут
- Тестируем отработку и сохранение (гуд)

5: +
- Описываем модель Incident
- Реализуем поля из MetricStorage
- Через Class Meta задаём название таблице incident_storage
- Создаем миграции
- Выполняем

6: +++ и тута. Отказ от сигнала в пользу ещё двух задач celery, которые вызываются в виде группы
через chain от задачи по сбору метрик
- Реализуем две задачи, на проверку уровней cpu/mem и disk
- Цель задач - поиск инцидентов на основе среднего значения % у метрик
- Тестируем работу задач (гуд)

7:
- Тестируем на всякий случай все ещё раз (гуд)

8: ++++
- Описываем Dockerfile
- Описываем docker-compose.yaml
- В нём описываем backend, db, celery_beat, celery_worker и redis


9:
- Льём на гит


11: Динамический пункт 
Осталось сделать README.md
