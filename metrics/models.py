from django.db import models

from index import models as index_mod
#Human
class Weighs(models.Model):
    human = models.ForeignKey(index_mod.Human, on_delete=models.CASCADE)
    m_date = models.DateTimeField('Дата') #Дата и время фиксации
    weigh = models.FloatField('Вес, кг')

    def __repr__(self):
        return str(self.m_date) + str(self.weigh)

    def __str__(self):
        return str(self.m_date) + str(self.weigh)

    def f_get_date_only(self):
        return self.m_date.date()

class Fitness(models.Model):
    human = models.ForeignKey(index_mod.Human, on_delete=models.CASCADE)
    m_date = models.DateTimeField('Дата')  # Дата и время фиксации

#Flowmeters
class Indication(models.Model):
    flowmeter = models.ForeignKey(index_mod.Flowmeter, on_delete=models.CASCADE)
    m_date = models.DateTimeField('Дата')
    indicate = models.FloatField('Показания')

class Communal(models.Model):
    flowmeter = models.ForeignKey(index_mod.Flowmeter, on_delete=models.CASCADE)
    m_date = models.DateTimeField('Дата')
    tarif = models.FloatField('Тариф')