from rest_framework import serializers

from .models import Competencia
from jugador.models import Jugador


class CompetenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competencia
        fields = '__all__'


class CrearCompetenciaSerializer(serializers.ModelSerializer):
    player_one = serializers.IntegerField()
    player_two = serializers.IntegerField()

    class Meta:
        model = Jugador
        fields = '__all__'

    def crear(self):
        print("Estoy en Crear")
        return {"ok"}

    def validate_player_one(self, param):
        print("Estoy en validate")
        return {"ok"}

