import os
import csv
import json

from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.utils import LayerMapping
from django.contrib.gis.geos import Point
from django.conf import settings
from django.db import transaction
from django.utils.text import slugify

from example.models import Area
from example.data.scripts.states import STATES

DB_CONN = 'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}'
DB_CONN_STR = DB_CONN.format(**settings.DATABASES['default'])

shapefile_filenames = ['cb_2018_{}_bg_500k.shp'.format(fips)
                       for fips in STATES.keys()]
shapefiles = [os.path.join('example', 'data', 'final', fname)
              for fname in shapefile_filenames]

class Command(BaseCommand):
    help = 'Load shapefile data into the database'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Importing shapefile data...'))
        self.import_areas()

    def import_areas(self):
        with transaction.atomic():
            # Truncate table, because otherwise LayerMapping will incorrectly
            # attempt to update the layer and mess up its geometry
            # See: https://stackoverflow.com/q/30300876
            Area.objects.all().delete()
            for shapefile in shapefiles:
                try:
                    assert os.path.exists(shapefile)
                except AssertionError:
                    msg = ('Required shapefile {} not found. '.format(shapefile) +
                           'Run `make all` from the data directory to download it.')
                    raise CommandError(msg)

                mapping = {
                    'id': 'GEOID',
                    'geom': 'POLYGON',
                }
                lm = LayerMapping(
                    model=Area,
                    data=shapefile,
                    mapping=mapping,
                    transform=False,
                    unique='id',
                )
                lm.save(progress=True, strict=True)

        self.stdout.write(self.style.SUCCESS('Imported Areas'))
