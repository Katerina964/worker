from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from .views import homePageView
from . import views

app_name = 'blog'

urlpatterns = [
    path('worker',views.homePageView, name='homePageView'),
    path('', views.python_developer, name='python_developer'),
    path('java_developer', views.java_developer, name='java_developer'),
    path('create_resume', views.create_resume, name='create_resume'),
    path('create_vacancy', views.create_vacancy, name='create_vacancy'),
    path('manage_resume', views.manage_resume, name='manage_resume'),
    path('manage_vacancy', views.manage_vacancy, name='manage_vacancy'),
    path('resume_list', views.resume_list, name='resume_list'),
    path('cabinet', views.cabinet, name='cabinet'),
    path('login', views.enter, name='enter'),
    path('auth_user', views.auth_user, name='auth_user'),
    path('update_resume/<int:pk>/', views.change_resume, name='change_resume'),
    path('update_vacancy/<int:pk>/', views.change_vacancy, name='change_vacancy'),
    path('resume_update/<int:pk>', views.update_resume, name='update_resume'),
    path('vacancy_update/<int:pk>', views.update_vacancy, name='update_vacancy'),
    path('resume/<int:pk>/', views.resume_detail, name='resume_detail'),
    path('vacancy/<int:pk>/', views.vacancy_detail, name='vacancy_detail'),
    path('delete_vacancy/<int:pk>/', views.delete_vacancy, name='delete_vacancy'),
    path('delete_resume/<int:pk>/', views.delete_resume, name='delete_resume'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
