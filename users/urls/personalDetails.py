from django.contrib import admin
from django.urls import path
from users.views.personalDetails import Personal_Details_View
from users.models.personalDetails import Personal_Details

urlpatterns = [
    path("personal_details/",Personal_Details_View.as_view()),
    path("update_personal_details/<int:pk>",Personal_Details_View.as_view()),
    path("get_personal_details/",Personal_Details_View.as_view()),
    path("get_personal_details/<int:pk>",Personal_Details_View.as_view()),
    path("delete_personal_details/<int:pk>",Personal_Details_View.as_view()),
]