# Generated by Django 3.1.2 on 2021-05-28 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sewa', '0016_kiospasar_tanggal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kiospasar',
            name='sewa',
            field=models.CharField(blank=True, choices=[('kios pasar', 'kios pasar')], max_length=200, null=True),
        ),
    ]
