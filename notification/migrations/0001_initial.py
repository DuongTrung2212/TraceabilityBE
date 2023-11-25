# Generated by Django 4.2.5 on 2023-11-25 15:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0006_product_is_delete'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_type', models.CharField(choices=[('COMMENT_PRODUCT', 'COMMENT_PRODUCT'), ('NONE', 'NONE')], default='NONE')),
                ('active', models.BooleanField(default=False)),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_notification', to=settings.AUTH_USER_MODEL)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_notification', to='product.product')),
            ],
        ),
    ]
