# Generated by Django 2.0.6 on 2018-10-13 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nsistanbul_job', '0005_auto_20180708_2001'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contributor',
            options={'ordering': ('order',)},
        ),
        migrations.AddField(
            model_name='contributor',
            name='order',
            field=models.PositiveIntegerField(default=10, verbose_name='Order'),
        ),
    ]
