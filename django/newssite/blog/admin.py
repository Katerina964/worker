from django.contrib import admin
from .models import  Author, Post, Resume


admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Resume)
