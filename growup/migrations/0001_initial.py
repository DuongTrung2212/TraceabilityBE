# Generated by Django 4.2.5 on 2023-10-04 03:43

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GrowUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField()),
                ('description', models.CharField()),
                ('image', django.contrib.postgres.fields.ArrayField(base_field=models.ImageField(upload_to=''), size=None)),
            ],
        ),
    ]
