from django.db import models
from django.db.models import Max

#Личность
class Human(models.Model):
    name = models.CharField(max_length=500)

class Human_Settings(models.Model):
    human = models.ForeignKey(Human, on_delete=models.CASCADE)
    c_date = models.DateTimeField('Дата') #Дата и время ввода значния
    set_name = models.CharField(max_length=100) #Название настройки: weigh_th
    set_val = models.CharField(max_length=250) #Значение настройки

    def __str__(self):
        return 'human-' + str(self.human_id) + '  ' + str(self.set_name) + '=' + str(self.set_val)
    #Метод возвращает последнее (текущее) значение (set_val) для set_name = weigh_th (порог веса)
    def get_weigh_th(self):
        return Human_Settings.objects.filter(human=self.human_id, set_name='weigh_th').order_by("-c_date")[0].set_val


#Счётчик
class Flowmeter(models.Model):
    name = models.CharField(max_length=500)