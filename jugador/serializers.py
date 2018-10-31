from rest_framework import serializers
from .models import Jugador
from team.models import Team


class JugadorSerializer(serializers.ModelSerializer):
    team = serializers.IntegerField()
    name = serializers.CharField()

    class Meta:
        model = Jugador
        fields = ('name', 'team')

    def validate_name(self, param):
        print(param)
        return param

    def validate_team(self, param):
        if Team.objects.filter(id=param):
            return param
        else:
            raise serializers.ValidationError('No existe el equipo')

    def create(self):
        player = Jugador()
        player.name = self.validated_data.get('name')
        player.team = Team.objects.get(id=self.validated_data.get('team'))
        print(self.validated_data.get('team'))
        print(self.validated_data.get('name'))
        player.save()
        return PlayerSerializer(player).data

    def show(self):
        player = Jugador.objects.all()
        print(player)
        return PlayerSerializer(player, many=True).data


class SearchSerializer(serializers.ModelSerializer):
    team = serializers.IntegerField()
    name = serializers.CharField()

    class Meta:
        model = Jugador
        fields = '__all__'

    def validate_name(self, param):
        if Jugador.objects.filter(name__icontains=param):
            return param
        else:
            raise serializers.ValidationError('No existe este jugador')

    def validate_team(self, param):
        if Team.objects.filter(id=param):
            return param
        else:
            raise serializers.ValidationError('No existe el equipo')

    def search(self):
        name = Jugador.objects.filter(name__icontains=self.validated_data.get('name'), team=self.validated_data.get('team'))
        return PlayerSerializer(name, many=True).data


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jugador
        fields = '__all__'


