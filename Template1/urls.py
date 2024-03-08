from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='template1'),
    path('<int:id>/', views.post, name='post'),
]
