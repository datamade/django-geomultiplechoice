import json
from django.forms.widgets import SelectMultiple


class GeoMultipleChoiceWidget(SelectMultiple):
    '''
    Widget for displaying and selecting multiple geometries.
    '''
    input_type = 'select'
    template_name = 'geomultiplechoice_widget.html'

    def __init__(self, attrs=None, choices=(), settings_overrides={}):
        """
        Override __init__ to update the config dictionary to make sure that the
        non-map input is always hidden.
        """
        self.settings_overrides = settings_overrides

        if attrs is None:
            updated_attrs = {'style': 'display:none'}
        else:
            updated_attrs = attrs.copy()
            updated_attrs['style'] = 'display:none'

        super().__init__(attrs=updated_attrs, choices=choices)

    def get_context(self, name, value, attrs):
        """
        Override get_context to create GeoJSON geometries to pass into the template.
        """
        context = super().get_context(name, value, attrs)

        MAP_LAYER_STYLE = {
          'color': '#7a7a7a',
          'weight': 3,
          'opacity': 0.5,
          'fillColor': '#999999',
          'fillOpacity': 0.3,
        }

        MAP_LAYER_SELECTED_STYLE = {
          'color': '#7a7a7a',
          'weight': 3,
          'opacity': 0.5,
          'fillColor': 'black',
          'fillOpacity': 0.7
        }

        settings_defaults = [
            ('MAP_ID', 'map'),
            ('MAP_LAYER_STYLE', MAP_LAYER_STYLE),
            ('MAP_LAYER_SELECTED_STYLE', MAP_LAYER_SELECTED_STYLE)
        ]

        for variable, default in settings_defaults:
            self.settings_overrides[variable] = \
                self.settings_overrides.get(variable, default)

        context['json'] = json.dumps({
            'type': 'FeatureCollection',
            'features': self.get_features()
        })

        context['settings_overrides'] = self.settings_overrides
        return context

    def format_value(self, value):
        """
        Override format_value to make sure that Array values get cast to
        Python lists properly. See: https://stackoverflow.com/a/53216766
        """
        if value is not None and not isinstance(value, (tuple, list)):
            value = value.split(',')
        return super().format_value(value)

    def get_features(self):
        return [{
                'type': 'Feature',
                'geometry': json.loads(choice.geom.json),
                'properties': {
                    'id': choice.pk,
                }
            }
            for _, choice in self.choices]
