# Generated by Django 2.0.3 on 2018-09-15 16:36

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import gp_projects.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PointFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', django.contrib.gis.db.models.fields.PointField(dim=3, srid=4326)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('altitude', models.FloatField(blank=True, null=True)),
                ('azimuth', models.FloatField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(blank=True, null=True, verbose_name='Image timestamp')),
                ('modifieddate', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to=gp_projects.models.userdata_directory_path)),
                ('thumbnail', models.ImageField(upload_to=gp_projects.models.userdata_directory_path)),
                ('text', models.TextField(blank=True, null=True, verbose_name='Text note')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TrackFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linestring', django.contrib.gis.db.models.fields.LineStringField(dim=3, srid=4326)),
                ('timestamp_start', models.DateTimeField(blank=True, null=True, verbose_name='Timestamp at start')),
                ('timestamp_end', models.DateTimeField(blank=True, null=True, verbose_name='Timestamp at end')),
                ('modifieddate', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(blank=True, null=True, verbose_name='Text note')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
