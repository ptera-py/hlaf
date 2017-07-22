from django.db import models

#Личность
class Human(models.Model):
    name = models.CharField(max_length=500)

    def tt(self):
        return Human.objects.all()