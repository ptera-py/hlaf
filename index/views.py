from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Human

#Главная страничка
def index(request):
    user_obj = request.user
    context = {'user_obj':user_obj,}
    return render(request,'index/index.html',context)

#Master data
def master_data(request):
    context ={'humans':Human.objects.all(), 'user_obj':request.user}
    return render(request, 'index/master_data.html',context)

#Human insert
def f_human_insert(request):
    human = Human(name=request.POST['human_name'])
    human.save()
    return HttpResponseRedirect(reverse('index:master_data'))

#Human delete
def f_human_delete(request):
    for human_id in request.POST.getlist('humans'):
        human = Human.objects.get(pk=human_id)
        human.delete()
    return HttpResponseRedirect(reverse('index:master_data'))