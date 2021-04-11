from django import forms
from django.forms import ModelForm

from searchapp.models import Search


class PostSearchForm(ModelForm):
    class Meta:
        model = Search
        fields = ['text']