# Generated by Django 3.2.9 on 2022-01-20 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0017_auto_20220120_1942'),
    ]

    operations = [
        migrations.RenameField(
            model_name='examresult',
            old_name='user_name',
            new_name='roll_no',
        ),
    ]
