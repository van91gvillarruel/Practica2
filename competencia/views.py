from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import CompetenciaSerializer, CrearCompetenciaSerializer

from .models import Competencia
from jugador.models import Jugador

class CompetenciaViewSet(viewsets.ModelViewSet):
    serializer_class = CompetenciaSerializer
    queryset = Competencia.objects.all()

    def create(self, request):
        print("Estoy en create")
        serializer = CrearCompetenciaSerializer(data=request.data, context=request.data)
        serializer.is_valid(raise_exception=True)
        resp = serializer.crear()
        return Response (resp)

    def list(self, request):
        print("estoy en lista")
        serializer = CompetenciaSerializer()
        respuesta = serializer.show()
        return Response(respuesta)



