from django.contrib import admin
from django.urls import path
from . import views
from .views import user_signup

urlpatterns = [
    path('', user_signup, name='users'),
]
