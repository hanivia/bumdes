# Generated by Django 3.1.2 on 2021-06-11 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sewa', '0068_customer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
    ]
