from rest_framework import serializers

from .models import Competencia
from jugador.models import Jugador
from team.models import Team
from random import randint


class CompetenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competencia
        fields = '__all__'


class CrearCompetenciaSerializer(serializers.ModelSerializer):

    def crear(self):
        print("Estoy en Crear")
        print(self.validated_data)
        competencia = Competencia()

        player_one = randint(0, 5)
        player_two = randint(0,5)

        if (player_one>player_two):
            print("gano jugador 1")
            print(player_one, player_two)
        elif (player_two>player_one):
            print("gano jugador 2")
            print(player_one, player_two)
        else:
            print("empate")
            print(player_one, player_two)

         # competencia.save()

        return {"ok"}


