from django.db.models import Q
from django.forms import forms
from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView

from searchapp.forms import PostSearchForm
from studyapp.models import Post


class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'searchapp/search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['text']
        post_list = Post.objects.filter(Q(post_title__icontains=searchWord) | Q(post_content__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)
