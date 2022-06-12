from django.contrib import admin

# Register your models here.
from denis.my_cv.models import Certificate,Denislav,Language,Project,ContactData,Work


@admin.register(Certificate)
class TaskCertificate(admin.ModelAdmin):
    list_display = ('name_en','name_de')

@admin.register(Denislav)
class TaskDenislav(admin.ModelAdmin):
    list_display = (
        'first_name','last_name'
        'mode',
    'about_me_en',
    'skills_first_en',
    'skills_second_en',
    'skills_third_en',
    'about_me_de',
    'skills_first_de' ,
    'skills_second_de',
    'skills_third_de'
                    )

@admin.register(Language)
class TaskLanguage(admin.ModelAdmin):
    list_display = ('language_en','level_en','language_de','level_de')


@admin.register(ContactData)
class TaskContactData(admin.ModelAdmin):
    list_display = (
    'git_hub',
    'linked_in',
    'phone',
    'email',)


@admin.register(Project)
class TaskProject(admin.ModelAdmin):
    list_display = (
    'title_en',
    'duration_en',
    'description_en',
    'used',
    'link',
    'demo',
    'source_code',
    'title_de',
    'duration_de',
    'description_de' )

@admin.register(Work)
class TaskWork(admin.ModelAdmin):
    list_display = (
    'from_date' ,
    'to_date',
    'position_en',
    'employer_en',
    'description_en',
    'position_de',
    'employer_de' ,
    'description_de'
    )