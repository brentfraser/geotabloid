# Generated by Django 2.0.3 on 2018-09-17 19:06

from django.conf import settings
import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import gp_projects.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gp_projects', '0003_auto_20180915_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('lat', models.FloatField(verbose_name='Latitude (WGS84)')),
                ('lon', models.FloatField(verbose_name='Longitude (WGS84)')),
                ('altitude', models.FloatField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
                ('modifieddate', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to=gp_projects.models.userdata_directory_path)),
                ('thumbnail', models.ImageField(upload_to=gp_projects.models.userdata_directory_path)),
                ('azimuth', models.FloatField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('lat', models.FloatField(verbose_name='Latitude (WGS84)')),
                ('lon', models.FloatField(verbose_name='Longitude (WGS84)')),
                ('altitude', models.FloatField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
                ('modifieddate', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Note type')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Text note')),
                ('form', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name='Form element')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='pointfeature',
            name='owner',
        ),
        migrations.DeleteModel(
            name='PointFeature',
        ),
        migrations.AddField(
            model_name='imagenote',
            name='note',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gp_projects.Note'),
        ),
        migrations.AddField(
            model_name='imagenote',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
