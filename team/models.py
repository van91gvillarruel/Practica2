from django.db import models

# Create your models here.

from django.db import models


class Team(models.Model):
    nombre = models.TextField(null=False, max_length=15)
