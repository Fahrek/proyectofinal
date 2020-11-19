"""buscajob URL Configuration

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
from apijob import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.vista_principal, name='home'),
    path('about/', views.about, name='about'),
    path('insert01/', views.insert_psycopg, name='ipsycopg'),
    path('insert02/', views.insert_pymysql, name='ipymsql'),
    path('select01/', views.select_psycopg, name='upsycopg'),
    path('select02/', views.select_pymysql, name='upymsql'),
    path('delete01/', views.delete_psycopg, name='dpsycopg'),
    path('delete02/', views.delete_pymysql, name='dpymsql'),
    path('anadir', views.vista_anadir, name='insertar'),
]
