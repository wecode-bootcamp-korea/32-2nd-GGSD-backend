# Generated by Django 4.0.4 on 2022-05-11 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applies', '0003_rename_projectapplystate_projectapplystatus_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectapplystatus',
            old_name='status',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='requeststatus',
            old_name='status',
            new_name='type',
        ),
    ]
