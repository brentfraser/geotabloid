# Generated by Django 2.0.3 on 2018-04-20 21:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0015_auto_20180417_1919'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modifieddate', models.DateTimeField(auto_now_add=True)),
                ('document', models.FileField(upload_to='documents/')),
                ('description', models.TextField(blank=True, null=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='document',
        ),
        migrations.RemoveField(
            model_name='project',
            name='owner',
        ),
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
