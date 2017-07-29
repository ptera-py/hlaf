from django.db import models

#Личность
class Human(models.Model):
    name = models.CharField(max_length=500)