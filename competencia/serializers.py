from rest_framework import serializers

from .models import Competencia
from jugador.models import Jugador
from jugador.serializers import JugadorInfoSerializer

from random import randint


class CompetenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competencia
        fields = '__all__'

    def show(self):
        competition = Competencia.objects.all()
        return CompetenciaInfoSerializer(competition, many=True).data


class CompetenciaInfoSerializer(serializers.Serializer):
    player_one = JugadorInfoSerializer()
    player_one_score = serializers.IntegerField()
    player_two = JugadorInfoSerializer()
    player_two_score = serializers.IntegerField()
    winner = serializers.IntegerField()
    played_time = serializers.DateTimeField()


class CrearCompetenciaSerializer(serializers.Serializer):
    player_one = serializers.IntegerField()
    player_two = serializers.IntegerField()

    def crear(self):
        competencia = Competencia()

        score1 = randint(0, 5)
        score2 = randint(0, 5)

        competencia.player_one_score=score1
        competencia.player_two_score=score2
        player1 = Jugador.objects.filter(id=self.validated_data.get('player_one')).first()
        player2 = Jugador.objects.filter(id=self.validated_data.get('player_two')).first()

        competencia.player_one = player1
        competencia.player_two = player2

        if (score1>score2):
            competencia.winner = player1.id

        elif (score2>score1):
            competencia.winner = player2.id

        competencia.save()

        return CompetenciaSerializer(competencia).data

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

