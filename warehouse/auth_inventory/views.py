from django.shortcuts import render, redirect
from .forms import RegisterForm



def index(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            
            return redirect("/register")
        else:
            form = RegisterForm()

    form = RegisterForm()
    return render(response, "register/register.html", {"form":form} )
