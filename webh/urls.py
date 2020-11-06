"""webh URL Configuration

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
from django.urls import path
from django.shortcuts import HttpResponse,render,redirect
from test_verify import views as viewzjw
from login import views
from mainForStu import views as mainView
from mainForTea import views as teacherView
urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'index_zjw/', viewzjw.index_zjw),
    path(r'login_zjw/', viewzjw.login_zjw),
    path(r'Mobileauthentication/', viewzjw.xiusj),
    path(r'Emailauthentication/', viewzjw.xiuyx),
    path(r'questions/', viewzjw.tq),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('teacher/', views.LoginForTeacher.as_view(), name="loginForTeacher"),
    path('main/', mainView.MainView.as_view(), name="main"),
    path('modify/', views.ModifyInformation.as_view(), name="modify"),
    path('getDataList/', teacherView.GetDataListView.as_view(), name="getDataList")
]
