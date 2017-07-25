from django.conf.urls import url

from . import views

app_name = 'metrics'
urlpatterns = [
    url(r'^$', views.f_menu, name='menu'),
    url(r'^weighs/$', views.f_weighs_editor, name='weighs_editor'),
    #input new weigh
    url(r'^weighs_insert/$', views.f_weigh_add, name='weighs_insert'),
    #delete weighs
    url(r'^weighs_delete/$', views.f_weigh_dell, name='weighs_delete'),
    #all idividual metrics
    url(r'^weighs/(?P<human_id>[0-9]+)/$', views.f_all_person_metrics, name='person_metrics'),
    #fitness
    url(r'^fitness/$', views.f_fitness_edit, name='fitness_editor'),
    #add fitness
    url(r'^fitness_insert/$', views.f_fitness_add, name='fitness_insert'),
    #delete fitness
    url(r'^fitness_delete/$', views.f_fitness_dell, name='fitness_delete'),
]
