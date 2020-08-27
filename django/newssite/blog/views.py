from django.shortcuts import render
from django.utils import timezone,dateformat
from .models import Post
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import F

def homePageView(request):
    post_list = Post.objects.all().order_by("-published_date")
    paginator = Paginator(post_list, 6)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    context = {'page_obj': page_obj}

    return render(request, 'blog/post_list.html', context)


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.quantity = F('quantity') + 1
    post.save()

    return render(request, 'blog/detail.html', {'post': post})
