from django.db import models

class Livro(models.Model):
    id = models.CharField(max_length=30, blank=True, primary_key=True)
    titulo = models.CharField(max_length=300)
    autor = models.CharField(max_length=200, blank=True, null=True)
    publicadora = models.CharField(max_length=100, blank=True, null=True)
    data_publicacao  = models.DateField(null=True, blank=True)
    numero_paginas = models.IntegerField(null=True, blank=True)  
    capa = models.TextField(blank=True) 
    sinopse = models.TextField(blank=True)      
    categoria = models.CharField(max_length=200, blank=True, null=True)
    valor = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return self.titulo
