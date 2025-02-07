from django.urls import path
from incident.views import IncidentListView


urlpatterns = [
    path('incidents/', IncidentListView.as_view(), name='incident-list'),
]
