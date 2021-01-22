from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *


def index(request):
    return render(request, template_name="login/index.html")


def welcome(request):
    user = request.POST.get("id_user")
    password = request.POST.get("pass")
    try:
        validation = User.objects.get(user_id=user)
    except User.DoesNotExist:
        return HttpResponse("Incorrect login details")
    if password != validation:
        return HttpResponse("Incorrect Password")
    return HttpResponse("Welcome %s" % user)
