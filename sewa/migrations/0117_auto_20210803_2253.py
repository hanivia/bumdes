# Generated by Django 3.1.2 on 2021-08-03 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sewa', '0116_auto_20210803_2245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pengeluaran',
            name='barang',
        ),
        migrations.AddField(
            model_name='tempbarang',
            name='total_transaksi',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='barang',
            name='image',
            field=models.ImageField(blank=True, default='fotokosong.gif', upload_to=''),
        ),
        migrations.AlterField(
            model_name='detailtransaksi',
            name='keterangan',
            field=models.CharField(choices=[('Bayar', 'Bayar'), ('Belum Bayar', 'Belum Bayar')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='detailtransaksi',
            name='pengembalian',
            field=models.CharField(blank=True, choices=[('Kembali', 'Kembali'), ('Belum Kembali', 'Belum Kembali')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='detailtransaksi',
            name='tanggal_kembali',
            field=models.DateTimeField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='penyewa',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='tempbarang',
            name='tanggal_kembali',
            field=models.DateTimeField(null=True),
        ),
    ]
