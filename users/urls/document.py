from django.contrib import admin
from django.urls import path
from users.views.document import Document_View
from users.views.all_data import All_Data_View
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("document/",Document_View.as_view()),
    path("update_document/<int:pk>",Document_View.as_view()),
    path("get_document/",Document_View.as_view()),
    path("get_document/<int:pk>",Document_View.as_view()),
    path("delete_document/<int:pk>",Document_View.as_view()),
    path("get_all_data/<int:pk>",All_Data_View.as_view()),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)