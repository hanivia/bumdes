# Generated by Django 3.1.2 on 2021-06-12 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sewa', '0078_orderitem_nik'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='nik',
        ),
    ]
