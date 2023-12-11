# Generated by Django 5.0 on 2023-12-11 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_benefits_why'),
    ]

    operations = [
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_count', models.CharField(max_length=255, verbose_name='Колличество студентов')),
                ('teacher_count', models.CharField(max_length=255, verbose_name='Колличество учителей')),
                ('mentors_count', models.CharField(max_length=255, verbose_name='Колличество менторов')),
                ('branches_count', models.CharField(max_length=255, verbose_name='Колличество филиалов')),
            ],
            options={
                'verbose_name': 'Цифры в курсе',
                'verbose_name_plural': 'Цифры в курсах',
            },
        ),
    ]
