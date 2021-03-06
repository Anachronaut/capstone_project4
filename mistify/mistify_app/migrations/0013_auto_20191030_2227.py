# Generated by Django 2.2.6 on 2019-10-31 03:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mistify_app', '0012_auto_20191030_2134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spot_un', models.CharField(max_length=100, verbose_name='spotify username')),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=2)),
                ('image', models.URLField(null=True)),
                ('playlist', models.CharField(max_length=200, null=True)),
                ('w_desc', models.CharField(max_length=100)),
                ('temp', models.CharField(max_length=5)),
                ('cloudy', models.CharField(max_length=100)),
                ('humid', models.CharField(max_length=100)),
                ('datetime', models.CharField(default='10:27 PM, Oct 3, 2019', max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Place',
        ),
    ]
