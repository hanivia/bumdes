# Generated by Django 3.1.2 on 2021-05-09 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sewa', '0008_auto_20210509_1236'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pengeluaran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal_Pengeluaran', models.CharField(blank=True, max_length=200, null=True)),
                ('keterangan_Pengeluaran', models.CharField(blank=True, max_length=200, null=True)),
                ('total_biaya', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Pengeluaran',
            },
        ),
    ]