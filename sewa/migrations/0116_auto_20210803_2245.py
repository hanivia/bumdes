# Generated by Django 3.1.2 on 2021-08-03 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sewa', '0115_remove_detailtransaksi_barang'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tempbarang',
            name='total_transaksi',
        ),
        migrations.RemoveField(
            model_name='transaksi',
            name='barang',
        ),
        migrations.RemoveField(
            model_name='transaksi',
            name='jml_pinjam',
        ),
        migrations.RemoveField(
            model_name='transaksi',
            name='jumlah',
        ),
        migrations.RemoveField(
            model_name='transaksi',
            name='keterangan',
        ),
        migrations.RemoveField(
            model_name='transaksi',
            name='pengembalian',
        ),
        migrations.RemoveField(
            model_name='transaksi',
            name='status',
        ),
        migrations.RemoveField(
            model_name='transaksi',
            name='tanggal_kembali',
        ),
        migrations.AddField(
            model_name='detailtransaksi',
            name='barang',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sewa.barang'),
        ),
        migrations.AddField(
            model_name='detailtransaksi',
            name='keterangan',
            field=models.CharField(choices=[('Bayar', 'Bayar'), ('Belum_bayar', 'Belum_bayar')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='detailtransaksi',
            name='pengembalian',
            field=models.CharField(blank=True, choices=[('Kembali', 'Kembali'), ('Belum_kembali', 'Belum_kembali')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='detailtransaksi',
            name='status',
            field=models.CharField(choices=[('Harian', 'Harian'), ('Tahunan', 'Tahunan')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pengeluaran',
            name='barang',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sewa.barang'),
        ),
        migrations.AlterField(
            model_name='barang',
            name='image',
            field=models.ImageField(blank=True, default='fotokosong.gif', upload_to='static/images/static/'),
        ),
        migrations.AlterField(
            model_name='detailtransaksi',
            name='tanggal_kembali',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='penyewa',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='tempbarang',
            name='tanggal_kembali',
            field=models.DateField(null=True),
        ),
    ]
