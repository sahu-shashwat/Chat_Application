from django.urls import path

from . import views


urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.custom_login, name="login"),
    path("logout/", views.custom_logout, name="logout"),
    path("create_room/", views.create_room, name="create_room"),
    path("", views.rooms, name="rooms"),
    path("<str:slug>", views.room, name="room"),
]