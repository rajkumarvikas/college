from django.contrib import admin
from django.urls import path
from myClass.views.myClass import myClassView
from users.views.all_data import All_Data_View
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("post_myclass/",myClassView.as_view()),
    path("update_myclass/<int:pk>",myClassView.as_view()),
    path("get_myclass/",myClassView.as_view()),
    path("get_myclass/<str:course>",myClassView.as_view()),
    path("delete_myclass/<int:pk>",myClassView.as_view()),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)