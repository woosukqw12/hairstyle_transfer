from django.urls import path
from .views import v3
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("v1/", views.v1, name="view 1"),
    #path("v2/", views.v2, name="view 2"),
    path("v3/", views.v3, name="view 3"),
    path("v4/", views.v4, name="view 4"),
    path('<int:inputed>/', views.v2, name='v22'),
    #path("upload/", views.upload, name="upload"),
    ]