# Generated by Django 3.1.2 on 2021-05-09 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sewa', '0009_pengeluaran'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pengeluaran',
            old_name='keterangan_Pengeluaran',
            new_name='pengeluaran',
        ),
        migrations.RenameField(
            model_name='pengeluaran',
            old_name='tanggal_Pengeluaran',
            new_name='tanggal_pengeluaran',
        ),
    ]