from django.urls import path

from . import views

urlpatterns = [
    path('', views.hello_main, name='hello_main'),
]