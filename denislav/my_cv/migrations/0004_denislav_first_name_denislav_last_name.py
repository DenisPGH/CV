# Generated by Django 4.0.5 on 2022-06-12 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_cv', '0003_work'),
    ]

    operations = [
        migrations.AddField(
            model_name='denislav',
            name='first_name',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='denislav',
            name='last_name',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
