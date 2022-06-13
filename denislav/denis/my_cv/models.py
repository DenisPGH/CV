from django.db import models

# Create your models here.
class Certificate(models.Model):
    CERTIFICATE_MAX_LENGHT=50
    name_en=models.CharField(max_length=CERTIFICATE_MAX_LENGHT)
    name_de=models.CharField(max_length=CERTIFICATE_MAX_LENGHT)


class Language(models.Model):
    LANGUAGE_MAX_LENGHT = 20
    language_en=models.CharField(max_length=LANGUAGE_MAX_LENGHT)
    level_en=models.CharField( max_length=LANGUAGE_MAX_LENGHT)

    language_de = models.CharField(max_length=LANGUAGE_MAX_LENGHT)
    level_de = models.CharField(max_length=LANGUAGE_MAX_LENGHT)




class ContactData(models.Model):
    PHONE_MAX_LENGHT=20
    git_hub=models.URLField()
    linked_in=models.URLField()
    phone=models.CharField( max_length=PHONE_MAX_LENGHT)
    email=models.EmailField()




class Denislav(models.Model):
    NAME_MAX_LENGHT=40
    first_name=models.CharField(max_length=NAME_MAX_LENGHT, null=True)
    last_name=models.CharField(max_length=NAME_MAX_LENGHT, null=True)
    mode=models.BooleanField( # if true is English, if False is Deutsch
        default=True
    )
    about_me_en=models.TextField()
    skills_first_en=models.TextField()
    skills_second_en=models.TextField()
    skills_third_en=models.TextField()

    about_me_de = models.TextField()
    skills_first_de = models.TextField()
    skills_second_de = models.TextField()
    skills_third_de = models.TextField()


class Project(models.Model):
    DURATION_MAX_LENGHT=50
    TITLE_MAX_LENGHT=50
    USED_MAX_LENGHT=50

    title_en=models.CharField(max_length=TITLE_MAX_LENGHT)
    duration_en=models.CharField(max_length=DURATION_MAX_LENGHT)
    description_en=models.TextField()
    used=models.CharField(max_length=USED_MAX_LENGHT)
    link=models.URLField()
    demo=models.URLField(null=True)
    source_code=models.URLField(null=True)

    title_de = models.CharField(max_length=TITLE_MAX_LENGHT)
    duration_de = models.CharField(max_length=DURATION_MAX_LENGHT)
    description_de = models.TextField()


class Work(models.Model):
    DURATION_MAX_LENGHT = 50
    TITLE_MAX_LENGHT = 50
    POSITION_MAX_LENGHT = 50

    from_date = models.DateField()
    to_date = models.DateField()

    position_en=models.CharField(max_length=POSITION_MAX_LENGHT)
    employer_en = models.CharField(max_length=TITLE_MAX_LENGHT)
    description_en = models.TextField()

    position_de = models.CharField(max_length=POSITION_MAX_LENGHT)
    employer_de = models.CharField(max_length=TITLE_MAX_LENGHT)
    description_de = models.TextField()



class Head(models.Model):
    HEAD_MAX_LENGHT=200
    head_en=models.CharField(max_length=HEAD_MAX_LENGHT)
    head_de=models.CharField(max_length=HEAD_MAX_LENGHT)
