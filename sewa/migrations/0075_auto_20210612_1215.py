# Generated by Django 3.1.2 on 2021-06-12 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sewa', '0074_orderitem_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pembayaran',
            name='user',
        ),
        migrations.AddField(
            model_name='pembayaran',
            name='nama',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
