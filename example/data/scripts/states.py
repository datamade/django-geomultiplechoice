# Relevant FIPS codes for geographic queries
US = '1'
# County codes are determined from CBSAs using the following crosswalk:
# https://www.uspto.gov/web/offices/ac/ido/oeip/taf/cls_cbsa/cbsa_countyassoc.htm#PartA1
# Region centroids are found by searching "${city} coordinates" for the primary
# city in each region. Zoom levels are configurable as a separate parameter for
# cases where the region is too large to fit the default zoom level, 11.
# Even though regions can span multiple states, each instance of the 'region'
# dictionary should have its own centroid and default_zoom -- this is necessary
# in order to support Python <3.6, where dictionaries are unordered by default.
STATES = {
    '17': { # The FIPS code of the state
        'name': 'Illinois', # The name of the state
        'regions': {
            'Chicago': { # The name of the region
                'counties': ['031'],
            },
        },
    },
}
