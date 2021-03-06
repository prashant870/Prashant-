# Generated by Django 3.0.1 on 2020-09-05 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('uniqueid', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=30)),
                ('rpassword', models.CharField(max_length=30)),
            ],
        ),
    ]
