# Generated by Django 3.1.2 on 2021-06-12 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sewa', '0085_auto_20210613_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('bayar', 'bayar')], default='belum bayar', max_length=200),
        ),
    ]
