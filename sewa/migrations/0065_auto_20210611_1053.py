# Generated by Django 3.1.2 on 2021-06-11 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sewa', '0064_auto_20210609_2229'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Register',
        ),
        migrations.AddField(
            model_name='customer',
            name='alamat',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='nama',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='nik',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='telepon',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
