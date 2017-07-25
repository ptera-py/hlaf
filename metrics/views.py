from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.core.urlresolvers import reverse

from index import models as index_mod
from . import models

#Меню редактирования метрик
def f_menu(request):
    context = {}
    return render(request, 'metrics/menu.html', context)

#Редактор веса
def f_weighs_editor(request):
    class Hum_We(): #Класс для передачи персоны + N последних взвешиваний
        human = '' #Содержит объект - персону
        weighs_N = '' #Содержит N объектов последних взвешиваний, связанных с human
    list_hum_we=[] #Список объектов Hum_We
    for human in index_mod.Human.objects.all():
        hum_we = Hum_We()
        hum_we.human = human
        hum_we.weighs_N = human.weighs_set.order_by('-m_date')[:10]
        list_hum_we.append(hum_we)

    context = {'user_obj':request.user, 'list_hum_we':list_hum_we}
    return render(request, 'metrics/weighs_redactor.html', context)

#Добавить вес
def f_weigh_add(request):
    human = get_object_or_404(index_mod.Human, pk=request.POST['human'])
    human.weighs_set.create(weigh=request.POST['weigh'].replace(',', '.'),m_date=timezone.now())
    return HttpResponseRedirect(reverse('metrics:weighs_editor'))

#Удалить вес
def f_weigh_dell(request):
    for weigh_id in request.POST.getlist('weighs'):
        weigh = models.Weighs.objects.get(pk=weigh_id)
        weigh.delete()
    return HttpResponseRedirect(reverse('metrics:weighs_editor'))

#Представление для вывода всех индивидуальных метрик по одному человеку
def f_all_person_metrics(request, human_id):
    human = get_object_or_404(index_mod.Human, pk=human_id)
    weighs = human.weighs_set.order_by('-m_date')
    context = {'Human':human, 'Weighs':weighs}
    return render(request,'metrics/person_weighs.html',context)

#Представление для ввода зарядки
def f_fitness_edit(request):
    class Hum_Fi():
        def __init__(self, hum, fit):
            self.human = hum
            self.fitness = fit
    l_hum_fi = []
    for human in index_mod.Human.objects.all():
        hum_fi = Hum_Fi(human,human.fitness_set.order_by('-m_date'))
        l_hum_fi.append(hum_fi)
    context = {'user_obj':request.user, 'l_hum_fi':l_hum_fi}
    return render(request, 'metrics/fitness_redactor.html', context)

#Добавить зарядку
def f_fitness_add(request):
    human = get_object_or_404(index_mod.Human, pk=request.POST['human'])
    human.fitness_set.create(m_date=timezone.now())
    return HttpResponseRedirect(reverse('metrics:fitness_editor'))

def f_fitness_dell(request):
    for fitness_id in request.POST.getlist('fitness'):
        fitness = models.Fitness.objects.get(pk=fitness_id)
        fitness.delete()
    return HttpResponseRedirect(reverse('metrics:fitness_editor'))