from django.shortcuts import render
from django.utils import timezone
from datetime import datetime,timedelta
from .models import Resume, Vacancy
from .forms import ResumeForm, VacancyForm
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.csrf import csrf_exempt
import requests
from django.db.models import F
import json
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_page
from itertools import chain
import os, time
from os import path


def homePageView(request):
    return render(request, 'blog/worker.html', )


def get_vacancies(request, keywords, position, cache_filename):
    if datetime.today().day == 1:
        month = datetime.now() - timedelta(days=61)
        vacancy = Vacancy.objects.filter(published_date__lt=month)
        vacancy.delete()
    worker_list = Vacancy.objects.filter(position__icontains=position)
    file_date = datetime.fromtimestamp(path.getmtime('/django/newssite/blog/cache/cache_python.txt'))
    delta_time = (datetime.now() - file_date).days
    print(delta_time,file_date)
    if delta_time > 0:
        try:
            url = "https://ru.jooble.org/api/46f8fbb2-41ac-4877-aa20-4b2479feb675"
            for page in range(1, 6):
                data = {
        	    "keywords": keywords,
        	    "page": str(page)}
                payload = requests.post(url, json=data)
                vacancies = payload.json()["jobs"]
                if page == 1:
                    vacancies_list = vacancies
                vacancies_list += vacancies
            with open(os.path.join('/django/newssite/blog/cache', cache_filename), 'w') as f:
                  f.write(json.dumps(vacancies_list))
        except:
            with open(os.path.join('/django/newssite/blog/cache', cache_filename), 'r') as f:
                   vacancies_lists = json.load(f)
    with open(os.path.join('/django/newssite/blog/cache', cache_filename), 'r') as f:
         vacancies_lists = json.load(f)
    vacancies_list = list(chain(worker_list, vacancies_lists))
    paginator = Paginator(vacancies_list, 6)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    context = {'page_obj': page_obj}
    return render(request, 'blog/vacancies_list.html', context)


@csrf_exempt
def python_developer(request):
    return get_vacancies(request, "python developer", "python", "cache_python.txt")


@csrf_exempt
def java_developer(request):
    return get_vacancies(request, "java developer", "java", "cache_java.txt")


def create_resume(request):
    form = ResumeForm()
    context = {'form': form}
    return render(request, 'blog/create_resume.html', context)


def create_vacancy(request):
    form = VacancyForm()
    context = {'form': form}
    return render(request, 'blog/create_vacancy.html', context)


def manage_questionnaire(request, class_form, type, key, template):
    user = authenticate(username=request.POST['email'],password= request.POST['password'])
    if user is None:
        try:
            user = User.objects.create_user(username=request.POST['email'], password=request.POST['password'])
        except:
            return render(request, 'blog/create_user.html')
    request.session["user"] = user.id
    form = class_form(request.POST)
    if form.is_valid():
        pk  = form.save().id
        owner = "YES"
    questionnaire = type.objects.get(pk=pk)
    questionnaire.user = user
    questionnaire.save()
    context = {key: questionnaire, 'owner':owner }
    return render(request, template, context)


def manage_vacancy(request):
    return  manage_questionnaire(request, VacancyForm, Vacancy, "vacancy", 'blog/vacancy.html' )


def manage_resume(request):
    return  manage_questionnaire(request, ResumeForm, Resume, "resume", 'blog/resume.html'  )


def resume_list(request):
    if datetime.today().day == 1:
        month = datetime.now() - timedelta(days=61)
        resumes = Resume.objects.filter(published_date__lt=month)
        resumes.delete()
    resume_list =Resume.objects.all().order_by("-published_date")
    paginator = Paginator(resume_list, 6)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    context = {'page_obj': page_obj}
    return render(request, 'blog/resume_list.html', context)


def cabinet(request):
    user_id= request.session.get("user", "red")
    if user_id != 'red':
        resumes = Resume.objects.filter(user=user_id).order_by("-published_date")
        vacancies = Vacancy.objects.filter(user=user_id).order_by("-published_date")
        cabinet_list = list(chain(resumes, vacancies))
    else:
        return render(request, "blog/create_user.html")
    paginator = Paginator(cabinet_list, 3)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    context = {'page_obj': page_obj}
    return render(request, 'blog/cabinet.html', context)


def enter(request):
    user = authenticate(username=request.POST['email'],password=request.POST['password'])
    if user:
        request.session["user"] = user.id
        return redirect('blog:cabinet')
    return render(request, "blog/create_user.html")


def create_user(request):
    user = authenticate(username=request.POST['email'],password=request.POST['password'])
    if user:
        request.session["user"] = user.id
        return redirect('blog:cabinet')
    context = {"user": user}
    return render(request, 'blog/create_user.html', context)


def change_resume(request, pk):
    resume = get_object_or_404(Resume,pk=pk)
    if request.method == "POST":
        form = ResumeForm(request.POST, instance=resume)
        form.save()
        resume.published_date = timezone.now()
        resume.save()
        owner = "YES"
        context = {'resume': resume, 'owner':owner }
        return render(request, 'blog/resume.html', context)
    else:
        form_resume = ResumeForm(instance=resume)
        context = {"form_resume":form_resume}
    return render(request, 'blog/change_resume_vacancy.html', context)


def change_vacancy(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    if request.method == "POST":
        form = VacancyForm(request.POST, instance=vacancy)
        form.save()
        vacancy.published_date = timezone.now()
        vacancy.save()
        owner = "YES"
        context = {'vacancy': vacancy,'owner':owner }
        return render(request, 'blog/vacancy.html', context)
    else:
        form = VacancyForm(instance=vacancy)
        context = {"form":form}
    return render(request, 'blog/change_resume_vacancy.html', context)


def update_resume(request, pk):
    resume = get_object_or_404(Resume,pk=pk)
    resume.published_date = timezone.now()
    resume.save()
    return redirect('blog:cabinet')


def update_vacancy(request, pk):
    vacancy = get_object_or_404(Vacancy,pk=pk)
    vacancy.published_date = timezone.now()
    vacancy.save()
    return redirect('blog:cabinet')


def resume_detail(request, pk):
    resume = Resume.objects.get(pk=pk)
    user_id= request.session.get("user", "red")
    owner = "NO"
    if  user_id == resume.user.id:
        owner = "YES"
        print(owner)
    context = {'resume': resume, 'owner':owner }
    return render(request, 'blog/resume.html', context)


def vacancy_detail(request, pk):
    vacancy= Vacancy.objects.get(pk=pk)
    user_id= request.session.get("user", "red")
    owner = "NO"
    if  user_id == vacancy.user.id:
        owner = "YES"
    context = {'vacancy': vacancy,'owner':owner }
    return render(request, 'blog/vacancy.html', context)


def delete_vacancy(request, pk):
    vacancy = get_object_or_404(Vacancy,pk=pk)
    vacancy.delete()
    return redirect('blog:cabinet')


def delete_resume(request, pk):
    resume= get_object_or_404(Resume,pk=pk)
    resume.delete()
    return redirect('blog:cabinet')
