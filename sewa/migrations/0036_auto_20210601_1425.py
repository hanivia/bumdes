# Generated by Django 3.1.2 on 2021-06-01 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sewa', '0035_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='qunatity',
            new_name='quantity',
        ),
    ]
