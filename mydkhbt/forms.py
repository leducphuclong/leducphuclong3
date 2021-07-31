from django import forms
from .models import Post
from django import forms
from .models import Comment
from django.db import models
from django.conf import settings


class UpdkhbtForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        self.post = kwargs.pop('post', None)
        super().__init__(*args, **kwargs)

    def save(self):
        updkhbt = super().save(commit=False)
        updkhbt.author = self.author
        updkhbt.post = self.post
        updkhbt.save()

    class Meta:
        model = Post
        fields = ["title", "body"]
        """exclude = ["date", "author", "date"]
        title = forms.CharField(label='Nhan đề', max_length=200)
        body = forms.CharField(label='Bài viết')"""


class CommentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        self.post = kwargs.pop('post', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.author = self.author
        comment.post = self.post
        comment.save()

    class Meta:
        model = Comment
        fields = ["body"]