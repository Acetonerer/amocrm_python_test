from rest_framework.generics import ListAPIView
from incident.models import Incident
from incident.serializers import IncidentSerializer


class IncidentListView(ListAPIView):
    """
    Представление для отображения всех инцидентов.
    """
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
