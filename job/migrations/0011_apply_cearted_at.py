# Generated by Django 3.1 on 2020-08-23 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0010_apply_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='cearted_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
