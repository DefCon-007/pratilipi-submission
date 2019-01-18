from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from webview.src import database as db
from django.contrib.auth.forms import UserCreationForm
from webview.models import userForm
import json
# Create your views here.
context_global = {}
context_global["cities"] = db.getAllCititesName()
context_global["userForm"] = userForm()
context_global["adminForm"] = UserCreationForm()

def home(request) :
    context = context_global.copy()
    if request.user.is_authenticated:

        return render(request, "webview/home.html", context)
    else :
        return redirect('login')


def pvrusers(request) :
    context = context_global.copy()
    context["userForm"] = userForm()
    if request.method == "POST" :
        form = userForm(request.POST)
        if form.is_valid() :
            form.save()
            context["alert"] = "User Added Successfully"
        else :
            context["alert"] = "There are some issues with the form data. Please check again"
    else :
        cityName  = request.GET.get('city')
        res = json.dumps({"data" : db.getAllUsersByCity(cityName)})
        if len(res) >=1 :
            return HttpResponse(res, status=200)
        else :
            return HttpResponse(status=404)
    return render(request, "webview/home.html", context)


def addNewAdmin(request) :
    context = context_global.copy()
    if request.method == "POST" :
        form = UserCreationForm(request.POST)
        if form.is_valid() :
            form.save()
            context["alert"] = "New admin user created successfully"
        else :
            context["alert"] = "There are some issues with the form data. Please check again"

    return render(request, "webview/home.html", context)