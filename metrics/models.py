from django.db import models

from index import models as index_mod
#Human
class Weighs(models.Model):
    human = models.ForeignKey(index_mod.Human, on_delete=models.CASCADE)
    m_date = models.DateTimeField('Дата') #Дата и время фиксации
    weigh = models.FloatField('Вес, кг')

class Fitness(models.Model):
    human = models.ForeignKey(index_mod.Human, on_delete=models.CASCADE)
    m_date = models.DateTimeField('Дата')  # Дата и время фиксации

#Flowmeters
class Indication(models.Model):
    flowmeter = models.ForeignKey(index_mod.Flowmeter, on_delete=models.CASCADE)
    m_date = models.DateTimeField('Дата')
    indicate = models.FloatField('Показания')