from rest_framework import serializers

from .models import Team


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

