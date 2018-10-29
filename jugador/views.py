from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .model import Jugador

class JugadorViewSet(viewsets.ModelViewSet):
    queryset = Jugador.objects.all()

    def list(self, request):
        print('servicio get')
        return Response('ok')