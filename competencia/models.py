from django.db import models


class Competencia(models.Model):
    # player_one = models.ForeignKey(null=False)
    player_one_score = models.IntegerField(null=False)
    # player_two = models.ForeignKey(null=False)
    player_two_score = models.IntegerField(null=False)
    played_time = models.DateTimeField(auto_now_add=True)
