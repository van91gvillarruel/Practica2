from rest_framework import viewsets
from .serializers import JugadorSerializer
from .models import Jugador
from rest_framework.response import Response


class JugadorViewSet(viewsets.ModelViewSet):
    serializer_class = JugadorSerializer
    queryset = Jugador.objects.all()

    def create(self, request):
        name = request.data['name']
        team = request.data['team']
        data1 = dict()
        data1['name'] = name
        data1['team'] = team
        print(data1)
        serializer = JugadorSerializer(data=data1)
        serializer.is_valid(raise_exception=True)
        respuesta = serializer.create()
        return Response(respuesta)