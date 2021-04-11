from django.urls import path


from mainapp import views
from studyapp.views import CategoryView, StudyListView, StudyDetailView

app_name = 'studyapp'

urlpatterns = [
    path('', CategoryView.as_view(), name='studyview'),
    path('<int:pk>/', StudyListView.as_view(), name='studylist'),
    path('detail/<int:pk>/', StudyDetailView.as_view(), name='studydetail'),
]