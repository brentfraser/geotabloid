# Generated by Django 2.0.3 on 2018-04-14 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_auto_20180414_2307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='profile',
        ),
        migrations.AddField(
            model_name='profile',
            name='projects',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.Project'),
        ),
    ]
