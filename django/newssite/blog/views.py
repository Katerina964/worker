from django.shortcuts import render
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Resume, Vacancy
from .forms import ResumeForm, VacancyForm
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
import requests
import json
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from itertools import chain
import os
from os import path
from django.core.mail import send_mail
from django.conf import settings


def homePageView(request):
    return render(request, 'blog/worker.html', )


def get_vacancies(request, keywords, position, cache_filename):
    if datetime.today().day == 1:
        month = datetime.now() - timedelta(days=61)
        vacancy = Vacancy.objects.filter(published_date__lt=month)
        vacancy.delete()
    worker_list = Vacancy.objects.filter(position__icontains=position)
    file_date = datetime.fromtimestamp(path.getmtime(f'/django/newssite/blog/cache/{cache_filename}'))
    delta_time = (datetime.now() - file_date).days
    print(delta_time, file_date)
    if delta_time > 0:

        try:
            url = "https://ru.jooble.org/api/46f8fbb2-41ac-4877-aa20-4b2479feb675"
            for page in range(1, 16):
                data = {"keywords": keywords, "page": str(page)}
                payload = requests.post(url, json=data)
                vacancies = payload.json()["jobs"]
                if page == 1:
                    vacancies_list = vacancies
                vacancies_list += vacancies
            with open(os.path.join('/django/newssite/blog/cache', cache_filename), 'w') as f:
                f.write(json.dumps(vacancies_list))
        except Exception:
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


def manage_questionnaire(request, class_form, type, key, template1, template2):
    form = class_form(request.POST)
    if form.is_valid():
        user = authenticate(username=request.POST['email'], password=request.POST['password'])
        if user is None:
            try:
                user = User.objects.create_user(username=request.POST['email'], password=request.POST['password'])
            except Exception:
                owner = "MISTAKE"
                context = {'form': form, 'owner': owner}
                return render(request, template2, context)
        pk = form.save().id
        owner = "YES"
        request.session["user"] = user.id
        questionnaire = type.objects.get(pk=pk)
        questionnaire.user = user
        questionnaire.save()
        context = {key: questionnaire, 'owner': owner}
        return render(request, template1, context)
    context = {'form': form}
    return render(request, template2, context)


def manage_vacancy(request):
    return manage_questionnaire(request, VacancyForm, Vacancy, "vacancy",
                                'blog/vacancy.html', 'blog/create_vacancy.html')


def manage_resume(request):
    return manage_questionnaire(request, ResumeForm, Resume, "resume", 'blog/resume.html', 'blog/create_resume.html')


def resume_list(request):
    if datetime.today().day == 1:
        month = datetime.now() - timedelta(days=61)
        resumes = Resume.objects.filter(published_date__lt=month)
        resumes.delete()
    resumes = Resume.objects.all().order_by("-published_date")
    paginator = Paginator(resumes, 6)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    context = {'page_obj': page_obj, 'resumes': resumes}
    return render(request, 'blog/resume_list.html', context)


def cabinet(request):
    user_id = request.session.get("user", "red")
    if user_id != 'red':
        resumes = Resume.objects.filter(user=user_id).order_by("-published_date")
        vacancies = Vacancy.objects.filter(user=user_id).order_by("-published_date")
        cabinet_list = list(chain(resumes, vacancies))
    else:
        return render(request, "blog/auth_user.html")
    paginator = Paginator(cabinet_list, 3)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    context = {'page_obj': page_obj}
    return render(request, 'blog/cabinet.html', context)


def enter(request):
    return render(request, "blog/auth_user.html")


def auth_user(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user:
            request.session["user"] = user.id
            return redirect('blog:cabinet')
    if request.method == "GET":
        try:
            email = request.GET['email']
            print(email)
            resume = Resume.objects.filter(email=email).last()
            print(resume)
            vacancy = Vacancy.objects.filter(email=email).last()
            if resume:
                password = resume.password
            if vacancy:
                password = vacancy.password
            print(password)
            send_mail('Ваш пароль', f'Ваш пароль: {password}.',
                      settings.EMAIL_HOST_USER,
                      [email])
            user = "YES"
            print(user)
        except Exception:
            user = "NO"
            print(user)
    context = {'user': user}
    return render(request, 'blog/auth_user.html', context)


def change_resume(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    if request.method == "POST":
        form_resume = ResumeForm(request.POST, instance=resume)
        if form_resume.is_valid():
            form_resume.save()
            resume.published_date = timezone.now()
            resume.save()
            owner = "YES"
            context = {'resume': resume, 'owner': owner}
            return render(request, 'blog/resume.html', context)
        else:
            print(form_resume.errors)
    else:
        form_resume = ResumeForm(instance=resume)
    context = {"form_resume": form_resume}
    return render(request, 'blog/change_resume_vacancy.html', context)


def change_vacancy(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    if request.method == "POST":
        form = VacancyForm(request.POST, instance=vacancy)
        if form.is_valid():
            form.save()
            vacancy.published_date = timezone.now()
            vacancy.save()
            owner = "YES"
            context = {'vacancy': vacancy, 'owner': owner}
            return render(request, 'blog/vacancy.html', context)
        else:
            print(form.errors)
    else:
        form = VacancyForm(instance=vacancy)
    context = {"form": form}
    return render(request, 'blog/change_resume_vacancy.html', context)


def update_resume(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    resume.published_date = timezone.now()
    resume.save()
    return redirect('blog:cabinet')


def update_vacancy(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    vacancy.published_date = timezone.now()
    vacancy.save()
    return redirect('blog:cabinet')


def resume_detail(request, pk):
    resume = Resume.objects.get(pk=pk)
    user_id = request.session.get("user", "red")
    owner = "NO"
    if user_id == resume.user.id:
        owner = "YES"
        print(owner)
    context = {'resume': resume, 'owner': owner}
    return render(request, 'blog/resume.html', context)


def vacancy_detail(request, pk):
    vacancy = Vacancy.objects.get(pk=pk)
    user_id = request.session.get("user", "red")
    owner = "NO"
    if user_id == vacancy.user.id:
        owner = "YES"
    context = {'vacancy': vacancy, 'owner': owner}
    return render(request, 'blog/vacancy.html', context)


def delete_vacancy(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    vacancy.delete()
    return redirect('blog:cabinet')


def delete_resume(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    resume.delete()
    return redirect('blog:cabinet')
