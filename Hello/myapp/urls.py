import imp
from django.urls import path
from myapp import views

urlpatterns = [
    path("", views.index, name="index"),
    path("counter", views.counter, name="counter"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("post/<str:user_request>", views.post, name="post"),
]
