# Generated by Django 3.1.2 on 2021-06-07 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sewa', '0052_pembayaran_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pembayaran',
            name='tag',
        ),
    ]