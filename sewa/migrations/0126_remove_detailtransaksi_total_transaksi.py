# Generated by Django 3.1.2 on 2021-08-13 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sewa', '0125_remove_tempbarang_total_transaksi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detailtransaksi',
            name='total_transaksi',
        ),
    ]