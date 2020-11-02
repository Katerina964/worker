from django.contrib import admin
from .models import  Author, Post, Resume, Vacancy


admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Resume)
admin.site.register(Vacancy)
