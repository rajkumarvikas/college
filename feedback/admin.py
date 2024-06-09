from django.contrib import admin
from feedback.models.feedback import Model_Feedback

@admin.register(Model_Feedback)

class Admin_Feedback(admin.ModelAdmin):
    list_display=['id','query_type','query_title','justify']
