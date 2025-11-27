from . import views
from django.urls import include, path

app_name = "squawk"
urlpatterns = [
    path("", views.Home, name="index"),
    path("about/", views.About, name="about"),
    path("squawks/", views.Squawk_list, name="squawk_list"),
    path("squawks/search/", views.Squawk_list, name="search_squawks"),

    path("squawks/create/", views.Squawk_create, name="squawk_create"),
    path("squawks/<int:squawk_id>/edit/", views.Squawk_edit, name="squawk_edit"),
    path("squawks/<int:squawk_id>/delete/", views.Squawk_delete, name="squawk_delete"),
    path("register/", views.register, name="register"),
    path("login/", include("django.contrib.auth.urls")),
    path("logout/", include("django.contrib.auth.urls")),

]