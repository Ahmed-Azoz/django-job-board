# Generated by Django 3.1 on 2020-08-22 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_auto_20200822_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('demail', models.EmailField(max_length=100)),
                ('website', models.FileField(upload_to='apply/')),
                ('cover_letter', models.CharField(max_length=500)),
            ],
        ),
    ]