"""Ustc_Lost_And_Found URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.shortcuts import redirect
from django.urls import path, re_path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve
from django.contrib.auth import views as auth_view
from . import settings, views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('lf/')),
    path('lf/', views.mainpage),
    path('lf/lf_release/', views.lf_release),
    path('report/', views.report),
    path('tips/', views.tips),
    path('qa/', views.qa),
    path('user/', views.user),
    path('api/lf/', include('lf.urls')),
    path('api/auth/', include('au.urls')),
    path('api/qa/', include('qa.urls')),
    path('login/', auth_view.LoginView.as_view(template_name='../templates/login.html'))
    #url(r'^static/(?P<path>.*)$',serve,{'document_root': settings.STATIC_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


'''
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''