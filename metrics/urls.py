from django.conf.urls import url

from . import views

app_name = 'metrics'
urlpatterns = [
    url(r'^$', views.f_menu, name='menu'),
    #url(r'^weighs/$', views.f_weighs_editor, name='weighs_editor'),
    #input new weigh
    url(r'^weighs_insert/$', views.f_weigh_add, name='weighs_insert'),
    #delete weighs
    url(r'^weighs_delete/$', views.f_weigh_dell, name='weighs_delete'),
    #all idividual metrics
    url(r'^weighs/(?P<human_id>[0-9]+)/$', views.f_all_person_metrics, name='person_metrics'),

    #fitness
    #add fitness
    url(r'^fitness_insert/$', views.f_fitness_add, name='fitness_insert'),
    #delete fitness
    url(r'^fitness_delete/$', views.f_fitness_dell, name='fitness_delete'),
    #all idividual fitnesses
    url(r'^fitness/(?P<human_id>[0-9]+)/$', views.f_all_person_fitness, name='person_fitnesses'),

    #flowmeter edit
    url(r'^indicate/$', views.f_indicate_edit, name='indicate_editor'),
    #add indicate
    url(r'^indicate_insert/$', views.f_indicate_add, name='indicate_insert'),
    #delete indicate
    url(r'^indicate_delete/$', views.f_indicate_dell, name='indicate_delete'),

    # communal edit
    url(r'^communal/$', views.f_communal_edit, name='communal_editor'),
    # add communal
    url(r'^communal_insert/$', views.f_communal_add, name='communal_insert'),
    # delete communal
    url(r'^communal_delete/$', views.f_communal_dell, name='communal_delete'),

    #########################
    #weghs all humans (generic) edit
    url(r'^weighs/$', views.f_generic_weighs, name='generic_weighs'),
    #input new weigh
    url(r'^weighs_add/$', views.f_weighs_add, name='weighs_add'),
    #del weigh
    url(r'^weighs_del/$', views.f_weighs_del, name='weighs_del'),

    #fitness all humans (generic) edit
    url(r'^fitness/$', views.f_generic_fitness, name='generic_fitness'),
    #add fitness
    url(r'^fitness_add/$', views.f_fitness_add, name='fitness_add'),
    #delete fitness
    url(r'^fitness_del/$', views.f_fitness_del, name='fitness_del'),
]