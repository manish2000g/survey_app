from django.urls import path
from . import views

urlpatterns = [
    path('get-surveys/', views.get_surveys, name='get_surveys'),
]
