

from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from commentapp.forms import CommentForm
from commentapp.models import Comment
from studyapp.models import Category, Post
from rest_framework.pagination import PageNumberPagination

class CategoryView(ListView):
    model = Category
    context_object_name = 'study_list'
    template_name = 'studyapp/list.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
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


class StudyListView(ListView):
    model = Post
    context_object_name = 'target_list'
    template_name = 'studyapp/studylist.html'
    paginate_by = 9

    def get_queryset(self):
        queryset = Post.objects.filter(category_id=self.kwargs['pk']).order_by('-created_date')
        return queryset


    def get_context_data(self, **kwargs):
        context = super(StudyListView, self).get_context_data(**kwargs)
        paginator = context['paginator']
        context['target_study_list'] = Category.objects.filter(id=self.kwargs['pk'])[:1]
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



class StudyDetailView(DetailView, FormMixin):
    model = Post
    form_class = CommentForm
    context_object_name = 'target_study_detail'
    template_name = 'studyapp/studydetail.html'







