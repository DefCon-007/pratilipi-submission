from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from webview.src import database as db
from django.contrib.auth.forms import UserCreationForm
from webview.models import userForm, movieForm
import json
from webview.src import utils

# Create your views here.
context_global = {}
try :
    context_global["cities"] = db.getAllCititesName()
except :
    pass
context_global["userForm"] = userForm()
context_global["adminForm"] = UserCreationForm()
context_global["movieForm"] = movieForm()
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
        print(cityName)
        context["userList"] = db.getAllUsersByCity(cityName)
        return render(request, "webview/users.html" , context)
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


def sendSingleMail(request) :
    email  = request.GET.get('mail')
    sub   = request.GET.get('sub')
    body  = request.GET.get('body')

    utils.sendSingleMail(email,sub,body)
    print("Mail sent")
    return HttpResponse("Email Sent Successfully")

def sendMovieNotification(request) :
    sub   = request.GET.get('sub')
    body  = request.GET.get('body')
    city = request.GET.get('city')

    emaiLlist = db.getAllUserEmailListByCity(city)

    print(emaiLlist)
    if len(emaiLlist) == 0 :
        return HttpResponse("No users in the city")
    try :
        utils.sendMultipleMails(emaiLlist, sub,body)
        return HttpResponse("Emails Sent Successfully")
    except :
        return HttpResponse("unable to send emails please try again")

def movie(request) :
    context = context_global.copy()
    if request.method == "POST" :
        form = movieForm(request.POST)
        if form.is_valid() :
            form.save()
            context["alert"] = "Movie Added Successfully"
        else :
            context["alert"] = "There are some issues with the form data. Please check again"
        #Adding new movie
        return render(request, "webview/home.html", context)

    cityName = request.GET.get('city')
    context["movie"] =  db.getAllMoviesByCityName(cityName)

    print(context["movie"] )
    if cityName :
        context["city"] = cityName
        return render(request, "webview/movie.html", context)
    else :
        return render(request, "webview/movie.html")


