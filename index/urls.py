from django.conf.urls import url

from . import views

app_name = 'index'
urlpatterns = [
    url(r'^$', views.index, name='index'),#index
    url(r'^master_data/$', views.master_data, name='master_data'),#master_data
    url(r'^master_data/human_insert', views.f_human_insert, name='human_insert'), #for human insert
    url(r'^master_data/human_delete', views.f_human_delete, name='human_delete'), #for human delete
]
