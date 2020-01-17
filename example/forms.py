from django import forms
from django.contrib.postgres.forms import SimpleArrayField
from django_geomultiplechoice.widgets import GeoMultipleChoiceWidget
from example.models import Area, SelectedArea


class ExampleGeoMultipleChoiceForm(forms.ModelForm):
    class Meta:
        model = SelectedArea
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        settings_overrides = {
            'DEFAULT_ZOOM': 12,
            'DEFAULT_CENTER': (41.88, -87.7),
            'RESET_VIEW' : True, # Defaults to True
            # Sets the bounds of RESET VIEW; y min, x min, y max, x max
            # See https://github.com/makinacorpus/django-leaflet/issues/192
            'SPATIAL_EXTENT': (-87.3, 41.5, -88, 42.15),
            'MAP_ID': 'my-example-map', # Defaults to 'map'
            'MAP_HEIGHT': '400px',
            'MAP_WIDTH': '100%',
            'MAP_LAYER_STYLE': {
              'color': '#7a7a7a',
              'weight': 3,
              'opacity': 0.5,
              'fillColor': '#999999',
              'fillOpacity': 0.3,
            },
            'MAP_LAYER_SELECTED_STYLE': {
              'color': '#7a7a7a',
              'weight': 3,
              'opacity': 0.5,
              'fillColor': 'black',
              'fillOpacity': 0.7
            }
        }

        self.fields['areas'].widget = GeoMultipleChoiceWidget(
            choices=[
                (choice.id, choice) for choice
                in Area.objects.all()
            ],
            settings_overrides=settings_overrides
        )
