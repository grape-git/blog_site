from django.urls import path

from searchapp.views import SearchFormView

app_name = 'searchapp'

urlpatterns = [
    path('', SearchFormView.as_view(), name='search'),
]