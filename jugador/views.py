from rest_framework import viewsets
from .serializers import JugadorSerializer, SearchSerializer
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

    #def list(self, request):
    #    serializer = JugadorSerializer()
    #    respuesta = serializer.show()
    #    return Response(respuesta)

    def list(self, request):
        data1= request.query_params.dict()
        print(data1)
        serializer = SearchSerializer(data=data1)
        serializer.is_valid(raise_exception=True)
        respuesta = serializer.search()
        return Response(respuesta)