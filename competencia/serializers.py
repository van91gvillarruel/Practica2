from rest_framework import serializers

from .models import Competencia
from jugador.models import Jugador
from jugador.serializers import JugadorSerializer


class CompetenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competencia
        fields = '__all__'


class CrearCompetenciaSerializer(serializers.Serializer):
    player_one = serializers.IntegerField()
    player_two = serializers.IntegerField()

    def crear(self):
        print("Estoy en Crear")
        return {"ok"}

    def validate_player_one(self, param):
        print("param validate 1: ")
        print(param)
        print(self.context)
        print("Estoy en validate 1")
        if Jugador.objects.filter(id=param):
            print(param)
            return param
        else:
            raise serializers.ValidationError("Jugador uno no existe")

    def validate_player_two(self, param):
        print(self.context)
        print("Estoy en validate 2")
        if Jugador.objects.filter(id=param):
            return param
        else:
            raise serializers.ValidationError("Jugador dos no existe")

    def validate(self, param):
        print(self.context)
        print("Estoy en validate 3")
        print(self.context)
        print(self.context['player_one'])
        p1 = Jugador.objects.filter(id=self.context['player_one'])
        p2 = Jugador.objects.filter(id=self.context['player_two'])
        print(JugadorSerializer(p1, many=True).data)
        print(JugadorSerializer(p2, many=True).data)

        return {'ok'}


