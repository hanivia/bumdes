# Generated by Django 3.1.2 on 2021-06-09 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sewa', '0063_auto_20210609_2208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pembayaran',
            name='nama',
        ),
        migrations.AddField(
            model_name='pembayaran',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
