# Generated by Django 3.1.2 on 2021-05-31 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sewa', '0032_register'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='user',
        ),
    ]