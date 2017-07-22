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
