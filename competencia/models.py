from django.db import models

from jugador.models import Jugador


class Competencia(models.Model):
    player_one = models.ForeignKey(Jugador, related_name='competencia_player_one', on_delete=models.CASCADE, null=True)
    player_one_score = models.IntegerField(null=False)
    player_two = models.ForeignKey(Jugador, related_name='competencia_player_two', on_delete=models.CASCADE, null=True)
    player_two_score = models.IntegerField(null=False)
    played_time = models.DateTimeField(auto_now_add=True)
