from django.urls import path

from projectapp.views import ProjectList, ProjectDetail

app_name = 'projectapp'

urlpatterns = [
    path('', ProjectList.as_view(), name='projectview'),
    path('<int:pk>/', ProjectDetail.as_view(), name='projectdetail'),
]