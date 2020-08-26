from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from .views import homePageView
from . import views

app_name = 'blog'

urlpatterns = [
    path('',views.homePageView, name='homePageView'),
    path('blog/<int:pk>/', views.detail, name='detail'),
]
