# Generated by Django 3.2.5 on 2021-09-14 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_profilemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]