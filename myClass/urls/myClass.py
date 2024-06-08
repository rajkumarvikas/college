from django.contrib import admin
from django.urls import path
from myClass.views.myClassPost import myClass_POST
from myClass.views.myClassDelete import myClass_DELETE
from myClass.views.myClassGet import myClass_Get
from users.views.all_data import All_Data_View
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("faculty/my-class/",myClass_POST),
    path("student/my-class/",myClass_Get),
    path("delete-my-class/<int:pk>",myClass_DELETE),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)