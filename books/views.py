from django.http import HttpResponse
from django.shortcuts import render
from . import models

#Стартовая страница
def f_start(request):
    caption = models.Book._meta.verbose_name
    cap_icon = 'glyphicon glyphicon-book'

    context = {'user_obj':request.user, 'caption':caption, 'cap_icon':cap_icon}
    return render(request, 'books/generic_books.html', context)

#Add/Edit Books
def f_edit(request):
    return HttpResponse('dsfd')