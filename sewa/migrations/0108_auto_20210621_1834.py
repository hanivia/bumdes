# Generated by Django 3.1.2 on 2021-06-21 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sewa', '0107_auto_20210621_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailtransaksi',
            name='pengembalian',
            field=models.CharField(blank=True, choices=[('kembali', 'kembali'), ('belumkembali', 'belumkembali')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='detailtransaksi',
            name='tanggal_kembali',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
