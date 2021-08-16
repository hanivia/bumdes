# Generated by Django 3.1.2 on 2021-05-29 17:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sewa', '0027_auto_20210529_2329'),
    ]

    operations = [
        migrations.AddField(
            model_name='penyewa',
            name='gambar',
            field=models.ImageField(blank=True, default='fotokosong.gif', upload_to=''),
        ),
        migrations.AddField(
            model_name='penyewa',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
