"""questionbox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from questions import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include ('rest_framework.urls')),
    path('questions/', views.questionList, name='question-list'),
    path('questions/<int:pk>/', views.questionDetail, name='question-detail'),
    path('questions/create/', views.questionCreate, name='question-create'),
    path('questions/<int:pk>/edit/', views.questionEdit, name='question-edit'),
    path('questions/<int:pk>/delete/', views.questionDelete, name='question-delete'),
    path('answers/', views.answerList, name='answer-list'),
    path('answers/<int:pk>/', views.answerDetail, name='answer-detail'),
    path('answers/create/', views.answerCreate, name='answer-create'),
    path('tags/', views.tagList, name='tag-list'),
    path('tags/<int:pk>/', views.tagDetail, name='tag-detail'),
    path('tags/create/', views.tagCreate, name='tag-create')


]


urlpatterns = format_suffix_patterns(urlpatterns)
