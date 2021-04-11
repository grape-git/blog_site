from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from commentapp.forms import CommentPJForm
from projectapp.models import Project


class ProjectList(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/projectlist.html'
    paginate_by = 9

    def get_queryset(self):
        queryset = Project.objects.all().order_by('-created_date')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ProjectList, self).get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5  # Display only 5 page numbers
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range
        return context


class ProjectDetail(DetailView, FormMixin):
    model = Project
    form_class = CommentPJForm
    context_object_name = 'project_detail'
    template_name = 'projectapp/projectdetail.html'