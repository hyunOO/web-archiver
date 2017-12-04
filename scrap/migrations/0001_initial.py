# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 14:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folderNumber', models.IntegerField(unique=True)),
                ('folderName', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('newsNumber', models.AutoField(primary_key=True, serialize=False)),
                ('newsName', models.CharField(max_length=20, unique=True)),
                ('newsFile', models.FileField(upload_to='')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='folder',
            name='newsNumber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scrap.News'),
        ),
        migrations.AddField(
            model_name='folder',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
