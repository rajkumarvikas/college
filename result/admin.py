from django.contrib import admin
from result.models.first import Sem_first
from result.models.second import Sem_second
from result.models.third import Sem_third
from result.models.fourth import Sem_fourth
from result.models.fifth import Sem_fifth
from result.models.sixth import Sem_sixth

# Register your models here.

@admin.register(Sem_first)
class Sem_first_admin(admin.ModelAdmin):
    list_display=('rid',
                  'semester',
                  'paper_code',
                  'paper_title',
                  'internal_marks',
                  'external_marks',
                  'obtain_marks'
                  )
    ordering=['rid','paper_code']
@admin.register(Sem_second)
class Sem_second_admin(admin.ModelAdmin):
    list_display=('rid',
                  'semester',
                  'paper_code',
                  'paper_title',
                  'internal_marks',
                  'external_marks',
                  'obtain_marks'
                  )
    ordering=['rid','paper_code']
@admin.register(Sem_third)
class Sem_third_admin(admin.ModelAdmin):
    list_display=('rid',
                  'semester',
                  'paper_code',
                  'paper_title',
                  'internal_marks',
                  'external_marks',
                  'obtain_marks'
                  )
    ordering=['rid','paper_code']
@admin.register(Sem_fourth)
class Sem_fourth_admin(admin.ModelAdmin):
    list_display=('rid',
                  'semester',
                  'paper_code',
                  'paper_title',
                  'internal_marks',
                  'external_marks',
                  'obtain_marks'
                  )
    ordering=['rid','paper_code']
@admin.register(Sem_fifth)
class Sem_fifth_admin(admin.ModelAdmin):
    list_display=('rid',
                  'semester',
                  'paper_code',
                  'paper_title',
                  'internal_marks',
                  'external_marks',
                  'obtain_marks'
                  )
    ordering=['rid','paper_code']
@admin.register(Sem_sixth)
class Sem_sixth_admin(admin.ModelAdmin):
    list_display=('rid',
                  'semester',
                  'paper_title',
                  'obtain_marks'
                #   'project_name',
                #   'seminar_presentation',
                #   'viva_voce',
                  )
    ordering=['rid']