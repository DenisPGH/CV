# Generated by Django 4.0.5 on 2022-06-12 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_cv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='denislav',
            name='mode',
            field=models.BooleanField(default=True),
        ),
    ]
