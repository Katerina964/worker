from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.core.paginator import Paginator
from django.views.generic import ListView

# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/post_list.html', {})

class HomePageView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    paginate_by = 6
