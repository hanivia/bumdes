# Generated by Django 3.1.2 on 2021-06-07 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sewa', '0054_delete_sewa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pengeluaran',
            old_name='keterangan_pengeluaran',
            new_name='keterangan',
        ),
    ]
