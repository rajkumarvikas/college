from django.contrib import admin
from django.urls import path
from users.views.registration import User_View
from users.models.registration import User_Model

urlpatterns = [
    path("register/",User_View.as_view()),
    path("update_register/<int:pk>",User_View.as_view()),
    path("get_register/",User_View.as_view()),
    path("get_register/<int:pk>",User_View.as_view()),
    path("delete_register/<int:pk>",User_View.as_view()),
]
