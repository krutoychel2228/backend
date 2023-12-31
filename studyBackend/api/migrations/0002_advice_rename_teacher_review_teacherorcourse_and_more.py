# Generated by Django 4.2.3 on 2023-07-03 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('text', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='review',
            old_name='teacher',
            new_name='teacherOrCourse',
        ),
        migrations.AddField(
            model_name='review',
            name='course',
            field=models.CharField(choices=[('first', '1 курс'), ('second', '2 курс'), ('third', '3 курс'), ('fourth', '4 курс')], default=1, max_length=200),
            preserve_default=False,
        ),
    ]
