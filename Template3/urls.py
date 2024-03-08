from django.urls import path
from . import views

urlpatterns = [
    path('', views.hobby, name='template3'),
]
