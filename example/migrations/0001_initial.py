# Generated by Django 3.0 on 2020-01-03 15:53

import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4269)),
            ],
        ),
        migrations.CreateModel(
            name='SelectedArea',
            fields=[
                ('name', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('areas', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=12), help_text='Select one or more areas on the map. Add or remove an area by clicking on it, or remove all areas by clicking the "Clear all" button.', size=None, verbose_name='Areas')),
            ],
        ),
    ]
