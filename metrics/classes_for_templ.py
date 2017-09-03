from django.utils import timezone
import datetime
from django.db.models import Avg, Count
from django.db import connection
from .models import Weighs

#Объект класса содержит конкретного Human и все значения одной метрики.
class OneMetric:
    #Конструктор принимает Human и object_set одной связанной метрики
    def __init__(self, human, l_ObjectSet, N=10):
        self.human = human
        self.metric_all = l_ObjectSet.order_by('-m_date')
        self.metric_N = l_ObjectSet.order_by('-m_date')[:N]
        self.model_fields = l_ObjectSet.model._meta.fields
        self.metric_all_l = [] #все значения метрики в виде списка списков
        for metric in self.metric_all:
            t_list=[] #промежуточный список
            for field in self.model_fields:
                t_list.append(getattr(metric,field.name))
            self.metric_all_l.append(t_list)
        self.metric_N_l = self.metric_all_l[:N]

#Класс для вывода веса содержит конкретного Human, и процедуры для вывода необходимых данных в шаблоне
class TemplateWeigh:
    def __init__(self, human, metric_set):
        self.human = human #Личность
        self.metrics_all = metric_set.order_by('-m_date') #Все объекты взвешиваний в обратном порядке
        self.metrics_6 = self.metrics_all[:6] #Шесть последних измерений
        self.metrics_10days = self.metrics_all.filter(m_date__gte = (datetime.date.today() - datetime.timedelta(days=10))) #Все взвешивания за последние 10 дней
        self.fields = metric_set.model._meta.fields[3:]
        self.metric_name = metric_set.model._meta.model_name
        #Построение данных для диаграмм в зависимости от типа метрики
        if (self.metric_name == 'weighs'):#для веса - средние данные по дням за последние 10 дней
            self.metrics_10days_aver = [] #Перечень средних весов за последние 10 дней [date, {'weigh':avg_weigh, 'count':count}]
            for i in range (11):
                t_date = datetime.date.today() - datetime.timedelta(days=i)
                t_weighs = self.metrics_all.filter(m_date__date=(t_date)).aggregate(weigh=Avg('weigh'), count=Count('m_date'))
                self.metrics_10days_aver.append([t_weighs, t_date])
        elif (self.metric_name == 'fitness'): #для зарядки кол-во зарядок в неделю за последние 10 недель
            self.metrics_10weeks_count = [] #перечень кол-ва зарядок в неделю за последние 10 недель [0-№ недели; 1-кол-во зарядок]
            for i in range(11):
                t_date = datetime.date.today() - datetime.timedelta(days=(7*i))
                t_week = t_date.strftime("%W")
                t_count = len(self.metrics_all.filter(m_date__week=t_week))
                self.metrics_10weeks_count.append([t_week, t_count])