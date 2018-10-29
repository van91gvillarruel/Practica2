from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Repsonse
from .model import Jugador

class JugadorViewSet(viewsets.ModelViewSet):


