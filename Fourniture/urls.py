"""
URL configuration for Fourniture project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path
from ManageObject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MemberCreate.as_view(), name="signUp"),
    path('signIn/', signIn, name="signIn"),
    path('signIn/login', login, name="login"),
    path('Home/<str:slug>', home, name="home"),
    path('Home/<str:slug>/createList', createListForm, name="createList"),
    path('Home/<str:slug>/createList/creation', creationList, name="creationList"),
    path('Home/<str:slug>/<str:list>/', addObject, name="addObject"),
    path('Home/<str:slug>/<str:list>/addingObject', addingObject, name="addingObject"),
    path('object/<str:slug>/<str:list>/<int:id>', deleteObject, name="deleteObject"),
    path('list/<str:slug>/<str:list>', deleteList, name="supList")
]

urlpatterns += staticfiles_urlpatterns()
