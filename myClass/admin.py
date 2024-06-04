from django.contrib import admin
from myClass.models.classPeriod import myClass

@admin.register(myClass)
class myClassAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'faculty_name',
        'date',
        'start',
        'end',
        'course',
        'description'
    )
