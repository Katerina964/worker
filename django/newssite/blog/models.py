from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Resume(models.Model):
    first_name = models.CharField(max_length=15, verbose_name='Имя', )
    surname = models.CharField(max_length=15, verbose_name='Фамилия', blank=True)
    position = models.CharField(max_length=50, verbose_name='Позиция',)
    town = models.CharField(max_length=15, verbose_name='Местоположение', blank=True)
    phone = models.CharField(max_length=30, verbose_name='Телефон')
    email = models.EmailField(max_length=30, verbose_name='Почта')
    password = models.CharField(max_length=20, verbose_name='Пароль')
    experience = models.TextField(verbose_name='Опыт работы')
    skills = models.TextField(verbose_name="Навыки")
    achievements = models.TextField(verbose_name='Достижения', blank=True)
    education = models.TextField(verbose_name='Образование')
    type_work = models.TextField(verbose_name='Вид занятости')
    addition = models.TextField(verbose_name='Дополнительно', blank=True)
    salary = models.CharField(max_length=20, verbose_name='Заработная плата', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="01")
    published_date = models.DateTimeField(default=timezone.now, verbose_name='Дата')

    def __str__(self):
        return self.first_name + " " + self.surname + " " + str(self.pk)


class Vacancy(models.Model):
    position = models.CharField(max_length=50, verbose_name='Позиция',)
    company = models.CharField(max_length=40, verbose_name='Kомпания')
    type_work = models.CharField(max_length=100, verbose_name='Вид занятости', )
    town = models.CharField(max_length=15, verbose_name='Местоположение')
    phone = models.CharField(max_length=30, verbose_name='Телефон')
    email = models.EmailField(max_length=30, verbose_name='Почта')
    password = models.CharField(max_length=20, verbose_name='Пароль',)
    description = models.TextField(verbose_name='Описание вакансии')
    responsibilities = models.TextField(verbose_name='Обязанности', blank=True)
    skills = models.TextField(verbose_name="Навыки")
    offer = models.TextField(verbose_name='Мы предлагаем')
    salary = models.CharField(max_length=20, verbose_name='Заработная плата', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="01")
    published_date = models.DateTimeField(default=timezone.now, verbose_name='Дата')

    def __str__(self):
        return self.company + " " + self.position
