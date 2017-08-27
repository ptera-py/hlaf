from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.core.urlresolvers import reverse

from index import models as index_mod
from . import models, classes_for_templ
from . import func_lib

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
    return func_lib.fl_obj_delete(request,models.Weighs,'metrics:weighs_editor')
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
    return func_lib.fl_obj_delete(request,models.Fitness,'metrics:fitness_editor')
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
def f_indicate_edit(request):
    list_hum_me = []  # Список объектов Hum_Me (Flowmeter + Metric)
    for flowmeter in index_mod.Flowmeter.objects.all():
        list_hum_me.append(classes_for_templ.OneMetric(flowmeter, flowmeter.indication_set,None))
    url_fordel = 'metrics:indicate_delete'
    url_foradd = 'metrics:indicate_insert'
    caption = ['Показания', 1]
    date_format = 's'
    context = {'user_obj': request.user, 'list_hum_me': list_hum_me, 'url_fordel': url_fordel, 'url_foradd': url_foradd,
               'caption': caption, 'date_format':date_format}
    return render(request, 'metrics/metric_redactor.html', context)
#Добавить показания
def f_indicate_add(request):
    flowmeter = get_object_or_404(index_mod.Flowmeter, pk=request.POST['human'])
    flowmeter.indication_set.create(indicate=request.POST['metric'].replace(',', '.'),m_date=timezone.now())
    return HttpResponseRedirect(reverse('metrics:indicate_editor'))
#Удалить показания
def f_indicate_dell(request):
    return func_lib.fl_obj_delete(request, models.Indication, 'metrics:indicate_editor')
##########################################################################################################

#Ввод данных по коммунальным тарифам
def f_communal_edit(request):
    list_hum_me = []  # Список объектов Hum_Me (Flowmeter + Metric)
    for flowmeter in index_mod.Flowmeter.objects.all():
        list_hum_me.append(classes_for_templ.OneMetric(flowmeter, flowmeter.communal_set, None))
    url_fordel = 'metrics:communal_delete'
    url_foradd = 'metrics:communal_insert'
    date_format = 's'
    caption = ['Тарифы', 1]
    context = {'user_obj': request.user, 'list_hum_me': list_hum_me, 'url_fordel': url_fordel, 'url_foradd': url_foradd,
               'caption': caption, 'date_format':date_format}
    return render(request, 'metrics/metric_redactor.html', context)
#Добавить тариф
def f_communal_add(request):
    flowmeter = get_object_or_404(index_mod.Flowmeter, pk=request.POST['human'])
    flowmeter.communal_set.create(tarif=request.POST['metric'].replace(',', '.'),m_date=timezone.now())
    return HttpResponseRedirect(reverse('metrics:communal_editor'))
#Удалить тариф
def f_communal_dell(request):
    return func_lib.fl_obj_delete(request, models.Communal, 'metrics:communal_editor')
##====================================================================================================
def f_generic_weighs(request):
    humans = index_mod.Human.objects.all()
    TemplateWeighs = []
    for human in index_mod.Human.objects.all():
        TemplateWeighs.append(classes_for_templ.TemplateWeigh(human))
    context = {'user_obj': request.user, 'humans': humans, 'TemplateWeighs':TemplateWeighs,}
    return render(request, 'metrics/generic_weighs.html', context)

#Добавить вес
def f_weighs_add(request):
    human = get_object_or_404(index_mod.Human, pk=request.POST['human'])
    human.weighs_set.create(weigh=request.POST['metric'].replace(',', '.'),m_date=timezone.now())
    return HttpResponseRedirect(reverse('metrics:generic_weighs'))

#Удалить вес
def f_weighs_del(request):
    return func_lib.fl_obj_delete(request, models.Weighs, 'metrics:generic_weighs')