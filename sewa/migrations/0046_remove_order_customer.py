# Generated by Django 3.1.2 on 2021-06-07 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sewa', '0045_orderitem_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
    ]
