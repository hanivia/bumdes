# Generated by Django 3.1.2 on 2021-08-03 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sewa', '0112_auto_20210803_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaksi',
            name='barang',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sewa.barang'),
        ),
        migrations.AddField(
            model_name='transaksi',
            name='jml_pinjam',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transaksi',
            name='jumlah',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transaksi',
            name='tanggal_kembali',
            field=models.DateTimeField(blank=True, max_length=200, null=True),
        ),
    ]
