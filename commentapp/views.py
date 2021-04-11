from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView

from commentapp.forms import CommentForm, CommentPJForm
from commentapp.models import Comment, CommentPJ
from projectapp.models import Project
from studyapp.models import Post


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'commentapp/create.html'

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = Post.objects.get(pk=self.request.POST['post_pk'])
        comment.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('studyapp:studydetail', kwargs={'pk':self.object.post.pk})


class CommentPJCreateView(CreateView):
    model = CommentPJ
    form_class = CommentPJForm
    template_name = 'commentapp/createpj.html'

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = Project.objects.get(pk=self.request.POST['project_pk'])
        comment.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('projectapp:projectdetail', kwargs={'pk':self.object.post.pk})