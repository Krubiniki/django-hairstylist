from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_barber_user, name='create_barber_user'),
]