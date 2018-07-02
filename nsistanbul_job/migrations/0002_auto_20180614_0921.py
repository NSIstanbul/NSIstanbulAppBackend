# Generated by Django 2.0.6 on 2018-06-14 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nsistanbul_job', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Is Deleted?'),
        ),
        migrations.AlterField(
            model_name='companyapp',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Is Deleted?'),
        ),
        migrations.AlterField(
            model_name='job',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Is Deleted?'),
        ),
    ]
