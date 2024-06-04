from django.contrib import admin
from django.urls import path
from faculty_login.views import faculty_View
from users.models.registration import User_Model

urlpatterns = [
    path("login/",faculty_View.as_view()),
]