# Generated by Django 3.1.2 on 2021-06-21 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sewa', '0108_auto_20210621_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='tempbarang',
            name='pengembalian',
            field=models.CharField(blank=True, choices=[('kembali', 'kembali'), ('belumkembali', 'belumkembali')], max_length=200, null=True),
        ),
    ]
