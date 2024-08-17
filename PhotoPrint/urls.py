from django.urls import path
from . import views

urlpatterns = [
    path('prices/', views.prices, name='prices'),
    path('', views.index, name='index'),
]
