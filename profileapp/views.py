from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from projectapp.models import Project


class ProjectList(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'profileapp/profile.html'

    def get_queryset(self):
        context = Project.objects.all().order_by('-created_date')[:5]
        return context