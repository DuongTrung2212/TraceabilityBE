# Generated by Django 4.2.5 on 2023-10-04 03:43

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(unique=True)),
                ('description', models.TextField()),
                ('banner', django.contrib.postgres.fields.ArrayField(base_field=models.ImageField(upload_to=''), size=None)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('product_type', models.CharField()),
                ('product_status', models.CharField()),
                ('active', models.BooleanField(default=False)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
