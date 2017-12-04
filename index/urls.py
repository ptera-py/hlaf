from django.conf.urls import url

from . import views

app_name = 'index'

urlpatterns = [
    #url(r'^$', views.index, name='index'),#index
    url(r'^$', views.index, name='index'),#index2

    url(r'^master_data/human$', views.master_data, name='master_data'),#master_data_human
    url(r'^master_data/human_insert', views.f_human_insert, name='human_insert'), #for human insert
    url(r'^master_data/human_delete', views.f_human_delete, name='human_delete'), #for human delete

    url(r'^master_data/flowmeter$', views.f_flowmeter_editor, name='flowmeter_editor'),#flowmeter_editor
    url(r'^master_data/flowmeter_insert', views.f_flowmeter_insert, name='flowmeter_insert'), #for flowmeter insert
    url(r'^master_data/flowmeter_delete', views.f_flowmeter_delete, name='flowmeter_delete'), #for flowmeter delete
##########################################################################
    #url(r'^index2/$', views.index2, name='index2'),#index2
    url(r'^master_data/essence/$', views.f_essence, name='essences'),#master_data_human
    url(r'^master_data/essence/add$', views.f_essence_add, name='essences_add'),#добавление или редактирование master_data_human
    url(r'^master_data/essence/del$', views.f_essence_del, name='essences_del'),#удаление master_data_human

    #url(f'^master_data/essence_settings$', views.f_essence_settings, name='essence_settings'),#

    url(r'^n_login/$', views.f_login, name='login'),#login
]
