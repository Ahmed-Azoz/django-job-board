# Generated by Django 3.1 on 2020-08-22 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_apply'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apply',
            old_name='demail',
            new_name='email',
        ),
    ]
