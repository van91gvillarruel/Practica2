from django.db import models
from team.models import Team


class Jugador(models.Model):
    name = models.TextField(null=True, max_length=50, )
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, default=None)

