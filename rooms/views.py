from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.

class PostList(generic.ListView):
    model = Post
    template_name = 'post_list.html'  # Specify the template name
    context_object_name = 'post_list'  # Specify the context object name