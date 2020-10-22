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
    surname = models.CharField(max_length=15, verbose_name='Фамилия')
    position = models.CharField(max_length=40, verbose_name='Позиция',help_text="Желаемая должность")
    town = models.CharField(max_length=15, verbose_name='Город')
    phone = models.CharField(max_length=30, verbose_name='Телефон')
    email = models.EmailField(max_length=25, verbose_name='Почта')
    password = models.EmailField(max_length=20, verbose_name='Пароль авторизации на сайте', help_text="Запомните пароль или запишите")
    experience = models.TextField( verbose_name='Опыт работы', help_text="Укажите  опыт в порядке убывания" )
    skills = models.CharField(max_length=500, verbose_name="Навыки")
    achievements = models.CharField(max_length=500, verbose_name='Достижения')
    education = models.CharField(max_length=300, verbose_name='Образование')
    type_work  = models.CharField(max_length=100, verbose_name='Вид занятости',
    help_text="Укажите важные для Вас критерии. Например: офис, удаленно, количество часов в день" )
    published_date = models.DateTimeField(
            default=timezone.now, verbose_name='Дата размещения')

    def __str__(self):
        return self.name + " " + self.surname
