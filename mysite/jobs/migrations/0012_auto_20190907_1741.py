# Generated by Django 2.2 on 2019-09-07 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0011_result'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicants',
            old_name='skills',
            new_name='matching_skills',
        ),
    ]
