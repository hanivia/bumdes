# Generated by Django 3.1.2 on 2021-06-19 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sewa', '0097_tempbarang_tanggal_kembali'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pengeluaran',
            old_name='total_biaya',
            new_name='biaya',
        ),
    ]
