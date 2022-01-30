# Generated by Django 3.2.9 on 2021-12-14 13:06

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_alter_questions_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0005_alter_examdetails_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examdetails',
            name='date',
            field=models.DateField(default=datetime.date(2021, 12, 14)),
        ),
        migrations.AlterUniqueTogether(
            name='examdetails',
            unique_together={('exam_id', 'student_id')},
        ),
    ]
