# Generated by Django 4.2.5 on 2023-11-21 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_alter_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
    ]
