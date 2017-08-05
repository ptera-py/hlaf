###Библиотека вспомогательных функций

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone

#Ф-я добавления элемента в таблицу БД

#DB_obj delete
def fl_obj_delete(req, dataset, redirect):
    for metric_id in req.POST.getlist('metric'):
        metric = dataset.objects.get(pk=metric_id)
        metric.delete()
    return HttpResponseRedirect(reverse(redirect))