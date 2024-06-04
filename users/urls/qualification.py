from django.contrib import admin
from django.urls import path
from users.views.qualification import Qualification_View

urlpatterns = [
    path("qualification/",Qualification_View.as_view()),
    path("update_qualification/<int:pk>",Qualification_View.as_view()),
    path("get_qualification/",Qualification_View.as_view()),
    path("get_qualification/<int:pk>",Qualification_View.as_view()),
    path("delete_qualification/<int:pk>",Qualification_View.as_view()),
]