# Generated by Django 2.2.6 on 2019-10-29 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mistify_app', '0006_place_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='image',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
