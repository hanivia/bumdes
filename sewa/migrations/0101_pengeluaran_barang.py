# Generated by Django 3.1.2 on 2021-06-20 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sewa', '0100_auto_20210620_0328'),
    ]

    operations = [
        migrations.AddField(
            model_name='pengeluaran',
            name='barang',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sewa.barang'),
        ),
    ]
