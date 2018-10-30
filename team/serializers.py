from rest_framework import serializers

from .models import Team

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class CreateTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = '__all__'

    def validate_nombre(self, param):
        print("validate team")
        if len(Team.objects.filter(nombre=param)) > 0:
            raise serializers.ValidationError("ya existe el Team")
        else:
            print("se creo Team")
            return param

    def crear(self):
        print("estoy en crear")
        print(self.validated_data)
        team = Team()
        team.nombre = self.validated_data.get('nombre')
        team.save()
        return CreateTeamSerializer(team).data


class ListTeamSerializer(serializers.Serializer):

    search = serializers.CharField(max_length=15, required=False)

    def listar(self):

        teams = Team.objects.filter(nombre__icontains=self.validated_data.get('search', ''))
        resp = TeamSerializer(teams, many=True).data
        return resp


