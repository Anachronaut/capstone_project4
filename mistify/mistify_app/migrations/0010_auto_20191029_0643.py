# Generated by Django 2.2.6 on 2019-10-29 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mistify_app', '0009_place_playlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='cloudy',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='humid',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='temp',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='w_desc',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Weather',
        ),
    ]
