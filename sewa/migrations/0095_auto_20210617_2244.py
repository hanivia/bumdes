# Generated by Django 3.1.7 on 2021-06-18 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sewa', '0094_auto_20210618_1039'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Angsuran',
        ),
        migrations.AddField(
            model_name='detailtransaksi',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='detailtransaksi',
            name='tanggal_kembali',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='barang',
            name='status',
            field=models.CharField(choices=[('harian', 'harian'), ('tahunan', 'tahunan')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='detailtransaksi',
            name='status',
            field=models.CharField(choices=[('harian', 'harian'), ('tahunan', 'tahunan')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='tempbarang',
            name='status',
            field=models.CharField(choices=[('harian', 'harian'), ('tahunan', 'tahunan')], max_length=200, null=True),
        ),
    ]