# Generated by Django 3.2.9 on 2022-01-21 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_newuser_randomnum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='randomnum',
            field=models.FloatField(default=0.9134208762902849),
        ),
    ]
