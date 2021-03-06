# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-01 20:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteStatusTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=120)),
                ('etd', models.DateTimeField(default=django.utils.timezone.now)),
                ('eta', models.DateTimeField()),
                ('arrival_datetime', models.DateTimeField(blank=True, null=True)),
                ('late_meal', models.BooleanField(default=False)),
                ('person', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StatusType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.AddField(
            model_name='sitestatustransaction',
            name='status_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.StatusType'),
        ),
    ]
