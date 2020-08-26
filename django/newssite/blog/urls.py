from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from .views import HomePageView
from . import views

app_name = 'blog'

urlpatterns = [
    # path(r'^$', views.post_list, name='post_list'),
    path('', HomePageView.as_view(), name='HomePageView'),
]
