from django.shortcuts import render, redirect
from webview.src import database as db
from webview.models import userForm
# Create your views here.
def home(request) :
    if request.user.is_authenticated:
        context = {}
        context["cities"] = db.getAllCititesName()
        context["userForm"] = userForm()
        return render(request, "webview/home.html", context)
    else :
        return redirect('login')


def pvrusers(request) :
    context = {}
    context["userForm"] = userForm()
    if request.method == "POST" :
        form = userForm(request.POST)
        if form.is_valid() :
            form.save()
            context["alert"] = "User Added Successfully"
        else :
            context["alert"] = "There are some issues with the form data. Please check again"
    return render(request, "webview/home.html", context)