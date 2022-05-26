import imp
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.show, name='show'),
    path('register', views.register, name='register' ),
    path('admin/', admin.site.urls),
]
