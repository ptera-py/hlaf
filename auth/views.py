from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

#Авторизация
class LoginFormView(generic.edit.FormView):
    form_class = AuthenticationForm
    success_url = '/'
    template_name = 'auth/login.html'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

#Logout
class LogoutView(generic.base.View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')
