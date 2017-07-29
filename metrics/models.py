from django.db import models

from index import models as index_mod

class Weighs(models.Model):
    human = models.ForeignKey(index_mod.Human, on_delete=models.CASCADE)
    m_date = models.DateTimeField('Дата') #Дата и время фиксации
    weigh = models.FloatField('Вес, кг')

class Fitness(models.Model):
    human = models.ForeignKey(index_mod.Human, on_delete=models.CASCADE)
    m_date = models.DateTimeField('Дата')  # Дата и время фиксации