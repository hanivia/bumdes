# Generated by Django 3.1.2 on 2021-06-19 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sewa', '0098_auto_20210620_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pengeluaran',
            name='biaya',
            field=models.BigIntegerField(blank=True, max_length=200, null=True),
        ),
    ]
