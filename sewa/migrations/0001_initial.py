# Generated by Django 3.1.2 on 2021-04-07 18:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='penyewa',
            fields=[
                ('id_penyewa', models.AutoField(primary_key=True, serialize=False)),
                ('nama_penyewa', models.CharField(max_length=200)),
                ('telp_penyewa', models.CharField(max_length=100)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'penyewa',
            },
        ),
        migrations.CreateModel(
            name='aset',
            fields=[
                ('id_unit', models.AutoField(primary_key=True, serialize=False)),
                ('fakultas', models.CharField(blank=True, max_length=200, null=True)),
                ('nama_dekan', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'aset',
            },
        ),
    ]
