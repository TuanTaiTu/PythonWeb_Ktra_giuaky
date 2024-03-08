from django.urls import path
from . import views

urlpatterns = [
    path('', views.characteristic, name='template2'),
]
