from django.db import models

class Jugador(models.Model):
    name = models.TextField(null=False, max_length=50)