from django.contrib import admin
from django.urls import path
from feedback.views.feedback import View_Feedback

urlpatterns = [
    path('feedback/',View_Feedback.as_view()),
]
