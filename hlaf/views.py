from django.http import HttpResponseRedirect, HttpResponse

#For redirect to indexpage
def red(request):
    return HttpResponseRedirect('/index/')