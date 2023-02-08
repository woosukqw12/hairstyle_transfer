from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("page1/", views.page1, name="page 1"),
    path("detectme", views.detectme, name="detectme"),
    path("page2/", views.page2, name="page 2"),
]

