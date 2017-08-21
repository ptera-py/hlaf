from django.db import models

#Личность
class Human(models.Model):
    name = models.CharField(max_length=500)

class Human_Settings(models.Model):
    human = models.ForeignKey(Human, on_delete=models.CASCADE)
    c_date = models.DateTimeField('Дата') #Дата и время ввода значния
    set_name = models.CharField(max_length=100) #Название настройки: weigh_th
    set_val = models.CharField(max_length=250) #Значение настройки


#Счётчик
class Flowmeter(models.Model):
    name = models.CharField(max_length=500)