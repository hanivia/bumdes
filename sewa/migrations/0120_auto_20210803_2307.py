# Generated by Django 3.1.2 on 2021-08-03 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sewa', '0119_auto_20210803_2305'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detailtransaksi',
            old_name='transaksi',
            new_name='total_transaksi',
        ),
    ]
