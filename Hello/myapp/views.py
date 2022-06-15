import email
from msilib.schema import Feature
from multiprocessing import context
from posixpath import split
from tkinter import Variable
from unicodedata import name
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature
from django.contrib.auth import authenticate


def index(request):

    features = Feature.objects.all()
    return render(request, "index.html", {"features": features})


def register(request):

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email1")
        password = request.POST.get("password")

        if User.objects.filter(email=email).exists():
            messages.info(request, "Email already Used")
            return redirect("register")
        elif User.objects.filter(username=username).exists():
            messages.info(request, "Username already Used")
            return redirect("register")
        else:
            user = User.objects.create_user(
                username=username, email=email, password=password
            )
            user.save()
            return redirect("login")
    else:
        print("No")

    return render(request, "register.html")


def login(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Credentials Invalid")

    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect("/")


def post(request, user_request):
    context = {"variable": Variable}
    return render(request, "post.html", {"variable": user_request})


def counter(request):

    text = request.POST["text"]
    amount_of_words = len(text.split())
    return render(
        request, "counter.html", {"amount": amount_of_words, "name": "kousher"}
    )
