from django.contrib import admin
from django.urls import path
from payment.views import Payment_views

urlpatterns = [
    path('users/payment/',Payment_views.as_view()),
]
