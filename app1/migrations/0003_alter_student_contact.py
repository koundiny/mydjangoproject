# Generated by Django 3.2.5 on 2022-05-30 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_rename_sid_student_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='contact',
            field=models.IntegerField(max_length=10),
        ),
    ]
