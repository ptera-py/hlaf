from django.conf.urls import url

from . import views

app_name = 'auth'
urlpatterns = [
    url(r'^login/', views.LoginFormView.as_view(), 'login'),
    url(r'^logout/', views.LogoutView.as_view(), 'logout'),
]
