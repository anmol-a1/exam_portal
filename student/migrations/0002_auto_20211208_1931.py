# Generated by Django 3.2.9 on 2021-12-08 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examdetails',
            name='obtained_marks',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='examdetails',
            name='result',
            field=models.CharField(default='NA', max_length=20),
        ),
    ]