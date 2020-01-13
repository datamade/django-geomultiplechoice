from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models as geo_models
from django.contrib.gis.geos import Point
from django.contrib.postgres import fields as pg_fields

class Area(models.Model):
    id = models.CharField(max_length=12, primary_key=True)
    geom = geo_models.MultiPolygonField(srid=4269)


class SelectedArea(models.Model):
    name = models.CharField(max_length=150, primary_key=True)
    areas = pg_fields.ArrayField(
        models.CharField(max_length=12),
        verbose_name='Areas',
        help_text=(
            'Select one or more areas on the map. '
            'Add or remove an area by clicking on it, or remove all areas '
            'by clicking the "Clear all" button.'
        )
    )
