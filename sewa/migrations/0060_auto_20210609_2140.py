# Generated by Django 3.1.2 on 2021-06-09 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sewa', '0059_remove_register_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='fotokosong.gif', upload_to='foto_pics'),
        ),
    ]
