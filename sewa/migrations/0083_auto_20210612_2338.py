# Generated by Django 3.1.2 on 2021-06-12 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sewa', '0082_auto_20210612_2331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal_pesan', models.DateTimeField(auto_now_add=True)),
                ('penyewa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sewa.penyewa')),
            ],
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sewa.order'),
        ),
    ]
