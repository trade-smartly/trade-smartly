from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r"^register[/]?$", views.register),
    re_path(r"^login[/]?$", views.login),
    re_path(r"^logout[/]?$", views.logout),
    re_path(r"^check-login[/]?$", views.check_login),
    re_path(r"^update[/]?$", views.update),
]
