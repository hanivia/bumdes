# Generated by Django 3.1.2 on 2021-06-21 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sewa', '0106_auto_20210621_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailtransaksi',
            name='tanggal_kembali',
            field=models.DateField(choices=[('kembali', 'kembali'), ('belumkembali', 'belumkembali')], null=True),
        ),
    ]