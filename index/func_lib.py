###Библиотека вспомогательных функций

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

#Ф-я добавления элемента в таблицу БД
#DB_obj insert
def fl_obj_insert(req, DB_obj, redirect):
    obj = DB_obj(name=req.POST['essence_name'])
    obj.save()
    return HttpResponseRedirect(reverse(redirect))
#DB_obj delete
def fl_obj_delete(req, DB_obj, redirect):
    for obj_id in req.POST.getlist('essences'):
        obj = DB_obj.objects.get(pk=obj_id)
        obj.delete()
    return HttpResponseRedirect(reverse(redirect))
