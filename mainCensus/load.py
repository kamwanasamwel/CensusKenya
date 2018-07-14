import os
from django.contrib.gis.utils import LayerMapping
from .models import nyeri

nyeri_mapping = {
    'const_code': 'CONST_CODE',
    'objectid_2': 'OBJECTID_2',
    'name': 'NAME',
    'objectid': 'OBJECTID',
    'constituen': 'CONSTITUEN',
    'county_ass': 'COUNTY_ASS',
    'spoilt': 'SPOILT',
    'county_a_1': 'COUNTY_A_1',
    'rejected': 'REJECTED',
    'reported': 'REPORTED',
    'spoilt_val': 'SPOILT_VAL',
    'valid': 'VALID',
    'disputed': 'DISPUTED',
    'result': 'RESULT',
    'county_cod': 'COUNTY_COD',
    'shape_leng': 'Shape_Leng',
    'county_nam': 'COUNTY_NAM',
    'shape_le_1': 'Shape_Le_1',
    'registered': 'REGISTERED',
    'shape_le_2': 'Shape_Le_2',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON',
}

nyeri_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'nyeri.shp'),
)

def run(verbose=True):
	lm = LayerMapping(nyeri, nyeri_shp, nyeri_mapping,transform=False,encoding='iso-8859-1',)
	lm.save(strict=True, verbose=verbose)