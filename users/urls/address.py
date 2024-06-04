from django.contrib import admin
from django.urls import path
from users.models.address import Address_Model
from users.views.address import Address_View

urlpatterns = [
    path("address/",Address_View.as_view()),
    path("get_address/<int:pk>",Address_View.as_view()),
    path("geta_ddress/",Address_View.as_view()),
    path("update_address/<int:pk>",Address_View.as_view()),
    path("delete_address/<int:pk>",Address_View.as_view()),
]