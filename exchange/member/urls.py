from django.urls import path
from . import views

urlpatterns = [
    path('', views.resort_list, name='index'),
]