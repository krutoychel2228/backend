# Generated by Django 4.2.3 on 2023-07-03 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_advice_rename_teacher_review_teacherorcourse_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='text',
        ),
    ]
