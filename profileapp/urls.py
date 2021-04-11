from django.urls import path

from profileapp.views import ProjectList

app_name = 'profileapp'

urlpatterns = [
     path('', ProjectList.as_view(), name='projectlist'),
]