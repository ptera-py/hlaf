from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Human, Flowmeter
from .func_lib import fl_obj_insert, fl_obj_delete

#Главная страничка
def index(request):
    user_obj = request.user
    context = {'user_obj':user_obj,}
    return render(request,'index/index.html',context)

#Главная страничка2
def index2(request):
    user_obj = request.user
    context = {'user_obj':user_obj,}
    return render(request,'index/base.html',context)

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