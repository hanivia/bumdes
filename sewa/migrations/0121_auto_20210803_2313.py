# Generated by Django 3.1.2 on 2021-08-03 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sewa', '0120_auto_20210803_2307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detailtransaksi',
            old_name='total_transaksi',
            new_name='transaksi',
        ),
    ]
