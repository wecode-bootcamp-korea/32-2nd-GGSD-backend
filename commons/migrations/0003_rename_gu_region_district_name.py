# Generated by Django 4.0.4 on 2022-05-11 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='region',
            old_name='gu',
            new_name='district_name',
        ),
    ]
