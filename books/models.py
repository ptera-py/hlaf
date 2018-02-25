from django.db import models
from django.contrib.auth.models import User

#Книга
class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.TextField(max_length=500) #Заголовок
    img = models.TextField(max_length=600) #Ссылка на картинку

    class Meta:
        verbose_name = 'Books'

#Авторы книги
class Book_Authors(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.TextField(max_length=500) #Имя автора


