from django.urls import path

from . import views
from .views import Allpost

app_name = 'mainapp'

urlpatterns = [
    path('', Allpost.as_view(), name='hello_main'),
]