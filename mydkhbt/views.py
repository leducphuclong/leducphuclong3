from .forms import UpdkhbtForm
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django import forms
from .models import Comment
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm
from django.http import HttpResponseRedirect
# Create your views here.


def up(request):
    form = UpdkhbtForm()
    if request.method == 'POST':
        form = UpdkhbtForm(request.POST, author=request.user, post=post)
        if form.is_valid():
            """Post.objects.create(title=form.cleaned_data['title'], body=form.cleaned_data['body'])"""
            form.save()
            return HttpResponseRedirect('/mydkhbt')
    return render(request, 'pages/updkhbt.html', {'form': form})


def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST, author=request.user, post=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    return render(request, "pages/postdkhbt.html", {"post": post, "form": form})

