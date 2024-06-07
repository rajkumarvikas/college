from django.contrib import admin
from django.urls import path
from result.views.first import Sem_first_Views
from result.views.second import Sem_second_Views
from result.views.third import Sem_third_Views
from result.views.fourth import Sem_fourth_Views
from result.views.fifth import Sem_fifth_Views
from result.views.sixth import Sem_sixth_Views
from result.views.all import *

urlpatterns = [
    path("first_semester/<int:rid>",Sem_first_Views.as_view()),
    path("second_semester/<int:rid>",Sem_second_Views.as_view()),
    path("third_semester/<int:rid>",Sem_third_Views.as_view()),
    path("fourth_semester/<int:rid>",Sem_fourth_Views.as_view()),
    path("fifth_semester/<int:rid>",Sem_fifth_Views.as_view()),
    path("sixth_semester/<int:rid>",Sem_sixth_Views.as_view()),
    path("all/",Result_All.as_view()),
]
