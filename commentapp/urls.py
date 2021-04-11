from django.urls import path

from commentapp.views import CommentCreateView, CommentPJCreateView

app_name = 'commentapp'

urlpatterns = [
    path('create/', CommentCreateView.as_view(), name='create'),
    path('createpj/', CommentPJCreateView.as_view(), name='createpj'),
]
