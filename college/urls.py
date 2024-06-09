
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/',include("users.urls.registration")),
    path('api/users/',include("users.urls.login")),
    path('api/users/',include("users.urls.personalDetails")),
    path('api/users/',include("users.urls.address")),
    path('api/users/',include("users.urls.qualification")),
    path('api/users/',include("users.urls.document")),
    path('api/',include("myClass.urls.myClass")),
    path('api/faculty/',include("faculty_login.urls")),
    path('api/student/',include("result.urls.result")),
    path('api/',include("feedback.urls.feedback")),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
