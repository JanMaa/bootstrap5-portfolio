from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('send-message/', views.createMessage, name="send-message")
]