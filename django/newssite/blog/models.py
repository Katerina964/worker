from django.db import models
from django.utils import timezone, dateformat
import datetime

class Author(models.Model):
    name =models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " " + self.surname

class Post(models.Model):
    author =  models.ForeignKey(Author, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    img = models.ImageField(upload_to='hairclip', verbose_name='photo', blank=True)
    published_date = models.DateTimeField(
            default=timezone.now)
    quantity=models.PositiveSmallIntegerField(default=1)


    def __str__(self):
        return self.title


class Resume(models.Model):
    first_name = models.CharField(max_length=15, verbose_name='Имя')
    surname = models.CharField(max_length=15, verbose_name='Фамилия', blank=True)
    position = models.CharField(max_length=50, verbose_name='Позиция',)
    town = models.CharField(max_length=15, verbose_name='Город', blank=True)
    phone = models.CharField(max_length=30, verbose_name='Телефон')
    email = models.EmailField(max_length=30, verbose_name='Почта')
    password = models.EmailField(max_length=20, verbose_name='Пароль')
    experience = models.TextField( verbose_name='Опыт работы',  )
    skills = models.TextField(verbose_name="Навыки")
    achievements = models.TextField( verbose_name='Достижения', blank=True)
    education = models.TextField( verbose_name='Образование')
    type_work  = models.TextField(verbose_name='Вид занятости')
    published_date = models.DateTimeField(
            default=timezone.now, verbose_name='Дата')

    def __str__(self):
        return self.name + " " + self.surname


class Vacancy(models.Model):

    position = models.CharField(max_length=50, verbose_name='Позиция',)
    company = models.CharField(max_length=40, verbose_name='Kомпания')
    type_work  = models.CharField(max_length=100, verbose_name='Вид занятости', )
    town = models.CharField(max_length=15, verbose_name='Город')
    phone = models.CharField(max_length=30, verbose_name='Телефон')
    email = models.EmailField(max_length=30, verbose_name='Почта')
    password = models.EmailField(max_length=20, verbose_name='Пароль',)
    description = models.TextField( verbose_name='Описание вакансии')
    responsibilities = models.TextField( verbose_name='Обязанности' )
    skills = models.CharField(max_length=500, verbose_name="Навыки")
    offer = models.TextField( verbose_name='Мы предлагаем')

    published_date = models.DateTimeField(
            default=timezone.now, verbose_name='Дата')


    def __str__(self):
        return self.company + " " + self.position
