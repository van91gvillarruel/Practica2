from rest_framework import serializers

from .models import Competencia
from jugador.models import Jugador

from random import randint


class CompetenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competencia
        fields = '__all__'


class CrearCompetenciaSerializer(serializers.Serializer):
    player_one = serializers.IntegerField()
    player_two = serializers.IntegerField()

# class CrearCompetenciaSerializer(serializers.ModelSerializer):

    def crear(self):
        print("Estoy en Crear")
        print(self.validated_data)
        competencia = Competencia()

        player_one = randint(0, 5)
        player_two = randint(0, 5)

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

    def validate_player_one(self, param):
        if Jugador.objects.filter(id=param):
            return param
        else:
            raise serializers.ValidationError("Jugador uno no existe")

    def validate_player_two(self, param):
        if Jugador.objects.filter(id=param):
            return param
        else:
            raise serializers.ValidationError("Jugador dos no existe")

    def validate(self, param):
        p1 = Jugador.objects.filter(id=self.context['player_one']).first()
        p2 = Jugador.objects.filter(id=self.context['player_two']).first()
        if p1.team.id != p2.team.id:
            return param
        else:
            raise serializers.ValidationError("Jugadores pertenecen al mismo equipo")

