from rest_framework import viewsets

from .serializers import CompetenciaSerializer

from .models import Competencia


class CompetenciaViewSet(viewsets.ModelViewSet):
    serializer_class = CompetenciaSerializer
    queryset = Competencia.objects.all()


