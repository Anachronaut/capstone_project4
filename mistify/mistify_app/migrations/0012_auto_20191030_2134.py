# Generated by Django 2.2.6 on 2019-10-31 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mistify_app', '0011_place_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='datetime',
            field=models.CharField(default='09:34 PM, Oct 3, 2019', max_length=50),
        ),
    ]
