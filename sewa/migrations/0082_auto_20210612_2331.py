# Generated by Django 3.1.2 on 2021-06-12 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sewa', '0081_auto_20210612_2301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
