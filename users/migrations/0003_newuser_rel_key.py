# Generated by Django 3.2.9 on 2021-12-07 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20211207_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='rel_key',
            field=models.EmailField(default='1111@gmail.com', max_length=254, verbose_name='email address'),
        ),
    ]
