from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone

from .models import Human, Flowmeter, Human_Settings
from .func_lib import fl_obj_insert, fl_obj_delete

#Главная страничка
def index(request):
    user_obj = request.user
    context = {'user_obj': user_obj,}
    return render(request,'index/index.html',context)

########Human
#Master data
def master_data(request):
    caption = 'HUMANS'
    url_fordel = 'index:human_delete'
    url_foradd = 'index:human_insert'
    context ={
        'essences':Human.objects.all(), 'user_obj':request.user, 'caption':caption, 'url_fordel':url_fordel, 'url_foradd':url_foradd,
    }
    return render(request, 'index/master_data.html',context)
#Human insert
def f_human_insert(request):
    return fl_obj_insert(request,Human,'index:master_data')
#Human delete
def f_human_delete(request):
    return fl_obj_delete(request,Human,'index:master_data')

########Flowmeter
#Master Data
def f_flowmeter_editor(request):
    caption = 'FLOW METERS'
    url_fordel = 'index:flowmeter_delete'
    url_foradd = 'index:flowmeter_insert'
    context ={
        'essences':Flowmeter.objects.all(), 'user_obj':request.user, 'caption':caption, 'url_fordel':url_fordel, 'url_foradd':url_foradd,
    }
    return render(request, 'index/master_data.html',context)
#Flowmeter insert
def f_flowmeter_insert(request):
    return fl_obj_insert(request,Flowmeter,'index:flowmeter_editor')
#Flowmeter delete
def f_flowmeter_delete(request):
    return fl_obj_delete(request,Flowmeter,'index:flowmeter_editor')

#####################################################################################
#Главная страничка2
def index2(request):
    user_obj = request.user
    context = {'user_obj':user_obj,}
    return render(request,'index/base.html',context)

#Настройка персоналий
def f_essence(request):
    user_obj = request.user
    context = {'user_obj': user_obj, 'essences':Human.objects.all(),}
    return render(request, 'index/essences.html', context)

#Добавление essence и essence settings
def f_essence_add(request):
    weigh_th = str(request.POST['ess_weigh_th']).strip()  # Порог веса, c удалением пробелов
    #Если создаётся новая запись
    if(not request.POST['human_id']):
        #Создаем новую запись в таблице Human
        ess = Human(name=request.POST['ess_nm'])
        ess.save()
        #Получаем настройки Human и если они не пустые, то пишем их в Human_Settings
        if (weigh_th != ''):
          ess_set = Human_Settings(human=ess, c_date=timezone.now(), set_name='weigh_th', set_val=weigh_th)
          ess_set.save()
    #Если редактируется имеющаяся
    else:
        # введённое значение не должно быть пустым и не должно быть равным текущему
        ess = Human.objects.get(pk=request.POST['human_id']) #Текущий human
        try: #Если создавать порог для human, у которого нет порога, то будет исключение AttributeError
            t_ess_set = ess.human_settings_set.first().get_weigh_th() #Порог веса для текущего human
        except AttributeError:
            t_ess_set = ''
        if ((weigh_th != '') and (weigh_th != t_ess_set)): #Соьственно, сама проверка
          ess_set = Human_Settings(human=ess, c_date=timezone.now(), set_name='weigh_th', set_val=weigh_th)
          ess_set.save()
    return HttpResponseRedirect(reverse('index:essences'))

#Персональные настройки
def f_essence_settings(request):
    return HttpResponse('ff')