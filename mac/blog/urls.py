from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="blogHome"),
    path("about/", views.about, name="blogHome"),
    path("blogpost/<int:id>", views.blogpost, name="blogHome")
]
