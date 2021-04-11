from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, TemplateView

from projectapp.models import Project
from studyapp.models import Post



class Allpost(ListView):
    model = Project
    context_object_name = 'project_post'
    template_name = 'mainapp/main.html'

    def get_queryset(self):
        context = Project.objects.all().order_by('-created_date')[:5]
        return context

    def get_context_data(self, **kwargs):
        context = super(Allpost, self).get_context_data(**kwargs)
        context['study_post'] = Post.objects.all().order_by('-created_date')[:9]
        return context
