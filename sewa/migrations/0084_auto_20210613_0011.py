# Generated by Django 3.1.2 on 2021-06-12 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sewa', '0083_auto_20210612_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('bayar', 'bayar'), ('belumbayar', 'belumbayar')], default='belumbayar', max_length=200),
        ),
    ]
