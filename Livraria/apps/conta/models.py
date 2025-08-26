from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    nome = models.CharField(max_length=200, blank=True)
    endereco = models.TextField(blank=True)

    def __str__(self):
            return self.username

