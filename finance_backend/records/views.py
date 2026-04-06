from rest_framework.viewsets import ModelViewSet
from .models import Record
from .serializers import RecordSerializer
from core.permissions import IsAdmin, IsAnalyst
from django_filters.rest_framework import DjangoFilterBackend


class RecordViewSet(ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type', 'category', 'date']

#  role based 
    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [IsAdmin()]
        return [IsAnalyst()]