from django.forms import ModelForm

from commentapp.models import Comment, CommentPJ


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['writer', 'email', 'comment_text']



class CommentPJForm(ModelForm):
    class Meta:
        model = CommentPJ
        fields = ['writer', 'email', 'comment_text']