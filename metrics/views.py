from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.core.urlresolvers import reverse

from index import models as index_mod
from . import models, classes_for_templ

#Меню редактирования метрик
def f_menu(request):
    context = {}
    return render(request, 'metrics/menu.html', context)

#Редактор веса
def f_weighs_editor(request):
    list_hum_me=[] #Список объектов Hum_Me (Human + Metric)
    for human in index_mod.Human.objects.all():
        list_hum_me.append(classes_for_templ.OneMetric(human, human.weighs_set))
    url_fordel = 'metrics:weighs_delete'
    url_foradd = 'metrics:weighs_insert'
    caption = ['Вес',1]
    context = {
        'user_obj':request.user, 'list_hum_me':list_hum_me, 'url_fordel':url_fordel, 'url_foradd':url_foradd, 'caption':caption,
    }
    return render(request, 'metrics/metric_redactor.html', context)
#Добавить вес
def f_weigh_add(request):
    human = get_object_or_404(index_mod.Human, pk=request.POST['human'])
    human.weighs_set.create(weigh=request.POST['metric'].replace(',', '.'),m_date=timezone.now())
    return HttpResponseRedirect(reverse('metrics:weighs_editor'))
#Удалить вес
def f_weigh_dell(request):
    for metric_id in request.POST.getlist('metric'):
        weigh = models.Weighs.objects.get(pk=metric_id)
        weigh.delete()
    return HttpResponseRedirect(reverse('metrics:weighs_editor'))
#Представление для вывода всех индивидуальных метрик по одному человеку
def f_all_person_metrics(request, human_id):
    human = get_object_or_404(index_mod.Human, pk=human_id)
    weighs = human.weighs_set.order_by('-m_date')
    list_hum_me=[] #Список объектов Hum_Me (Human + Metric)
    list_hum_me.append(classes_for_templ.OneMetric(human, weighs, None))
    url_fordel = 'metrics:weighs_delete'
    url_foradd = 'metrics:weighs_insert'
    caption = ['Вес',0]
    context = {
        'user_obj':request.user, 'list_hum_me':list_hum_me, 'url_fordel':url_fordel, 'url_foradd':url_foradd, 'caption':caption,
    }
    return render(request,'metrics/metric_redactor.html',context)
#############################################################################################

#Представление для ввода зарядки
def f_fitness_edit(request):
    list_hum_me=[] #Список объектов Hum_Me (Human + Metric)
    for human in index_mod.Human.objects.all():
        list_hum_me.append(classes_for_templ.OneMetric(human, human.fitness_set))
    url_fordel = 'metrics:fitness_delete'
    url_foradd = 'metrics:fitness_insert'
    caption = ['Зарядка',1]
    context = {'user_obj':request.user, 'list_hum_me':list_hum_me, 'url_fordel':url_fordel, 'url_foradd':url_foradd, 'caption':caption}
    return render(request, 'metrics/metric_redactor.html', context)
#Добавить зарядку
def f_fitness_add(request):
    human = get_object_or_404(index_mod.Human, pk=request.POST['human'])
    human.fitness_set.create(m_date=timezone.now())
    return HttpResponseRedirect(reverse('metrics:fitness_editor'))
def f_fitness_dell(request):
    for fitness_id in request.POST.getlist('metric'):
        fitness = models.Fitness.objects.get(pk=fitness_id)
        fitness.delete()
    return HttpResponseRedirect(reverse('metrics:fitness_editor'))
#Представление для вывода всех индивидуальных метрик по одному человеку
def f_all_person_fitness(request, human_id):
    human = get_object_or_404(index_mod.Human, pk=human_id)
    fitnessess = human.fitness_set.order_by('-m_date')
    list_hum_me=[] #Список объектов Hum_Me (Human + Metric)
    list_hum_me.append(classes_for_templ.OneMetric(human, fitnessess, None))
    url_fordel = 'metrics:fitness_delete'
    url_foradd = 'metrics:fitness_insert'
    caption = ['Зарядка',0]
    context = {
        'user_obj':request.user, 'list_hum_me':list_hum_me, 'url_fordel':url_fordel, 'url_foradd':url_foradd, 'caption':caption,
    }
    return render(request,'metrics/metric_redactor.html',context)
####################################################################################################

#Ввод данных по счётчикам
def f_flowmeter_edit(request):
    b = models.Fitness.objects.all()
    return HttpResponse(str(b))