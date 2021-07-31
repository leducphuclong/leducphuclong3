from django.urls import path
from .models import Post
from django.views.generic import ListView, DetailView
from mydkhbt import views as mydkhbt_views
from django.urls import path
from . import views
from django.views.generic import ListView, DetailView
from .models import Post


urlpatterns = [
    path('', ListView.as_view(
        queryset=Post.objects.all().order_by('-date'),
        template_name='pages/mydkhbt.html',
        context_object_name='Posts',
        paginate_by=10),
        name='mydkhbt'),
    path('<int:pk>/', mydkhbt_views.post, name='postdkhbt'),
    path('updkhbt/', mydkhbt_views.up, name='updkhbt'),
]
