from django.shortcuts import render
from django.utils import timezone,dateformat
from .models import Post, Resume
from .forms import ResumeForm, VacancyForm
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.csrf import csrf_exempt
import requests
from django.db.models import F
import json

def homePageView(request):
    post_list = Post.objects.all().order_by("-published_date")

    for post in post_list:
        post.text = post.text[0:500] + "  . . ."

        post.published_date = str(dateformat.format(post.published_date, 'Y-m-d H:i:s'))[0:10]
        # post.pupublished_date.save()

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
@csrf_exempt
def python_developer(request):
    # url = "https://ru.jooble.org/api/46f8fbb2-41ac-4877-aa20-4b2479feb675"
    # data = {
	# 	"keywords": "python developer",
	# 	"page": "1"}
    # vacancies = requests.post(url, data=data)
    # vacancies_list = vacancies.json()
    # vacancies_list = json.loads(vacancies)
    with open('/django/newssite/blog/json/python.json', 'rt') as f:
         vacancies_list = json.load(f)
    vacancies_list = vacancies_list["jobs"]


    paginator = Paginator(vacancies_list, 6)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    context = {'page_obj': page_obj}

    return render(request, 'blog/vacancies_list.html', context)

@csrf_exempt
def java_developer(request):
    # url = "https://ru.jooble.org/api/46f8fbb2-41ac-4877-aa20-4b2479feb675"
    # data = {
	# 	"keywords": "python developer",
	# 	"page": "1"}
    # vacancies = requests.post(url, data=data)
    # vacancies_list = vacancies.json()
    # vacancies_list = json.loads(vacancies)
    with open('/django/newssite/blog/json/java.json', 'rt') as f:
         vacancies_list = json.load(f)
    vacancies_list = vacancies_list["jobs"]


    paginator = Paginator(vacancies_list, 6)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    context = {'page_obj': page_obj}

    return render(request, 'blog/vacancies_list.html', context)



def create_resume(request):
    form = ResumeForm()
    context = {'form': form}
    return render(request, 'blog/create_resume.html', context)

def create_vacancy(request):
    form = VacancyForm()
    context = {'form': form}
    return render(request, 'blog/create_vacancy.html', context)
