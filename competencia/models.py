from django.db import models

# Create your models here.
class Jugador(models.Model):
    name = models.TextField(nul=False, max_length=50)

