# Generated by Django 2.2.6 on 2019-10-29 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mistify_app', '0004_place_spot_un'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='spot_un',
            field=models.CharField(max_length=100, verbose_name='spotify username'),
        ),
    ]
