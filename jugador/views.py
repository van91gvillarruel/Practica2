from rest_framework import viewsets
from .serializers import JugadorSerializer
from .models import Jugador

class JugadorViewSet(viewsets.ModelViewSet):
    serializer_class = JugadorSerializer
    queryset = Jugador.objects.all()