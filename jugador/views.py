from rest_framework import viewsets
from .serializers import JugadorSerializer
from .models import Jugador
from rest_framework.response import Response


class JugadorViewSet(viewsets.ModelViewSet):
    serializer_class = JugadorSerializer
    queryset = Jugador.objects.all()



