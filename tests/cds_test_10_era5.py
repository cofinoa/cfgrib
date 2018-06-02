
import pytest

import eccodes_grib

import cdscommon


TEST_FILES = {
    'era5-single-levels-reanalysis': [
        'reanalysis-era5-single-levels',
        {
            'variable': '2m_temperature',
            'product_type': 'reanalysis',
            'year': '2017',
            'month': '01',
            'day': '01',
            'time': ['00:00', '12:00'],
            'grid': ['3', '3'],
            'format': 'grib',
        },
        191,
    ],
    'era5-single-levels-ensemble_members': [
        'reanalysis-era5-single-levels',
        {
            'variable': '2m_temperature',
            'product_type': 'ensemble_members',
            'year': '2017',
            'month': '01',
            'day': '01',
            'time': ['00:00', '12:00'],
            'grid': ['3', '3'],
            'format': 'grib',
        },
        192,
    ],
    'era5-pressure-levels-reanalysis': [
        'reanalysis-era5-pressure-levels',
        {
            'variable': 'temperature',
            'pressure_level': ['500', '850'],
            'product_type': 'reanalysis',
            'year': '2017',
            'month': '01',
            'day': '01',
            'time': ['00:00', '12:00'],
            'grid': ['3', '3'],
            'format': 'grib',
        },
        191,
    ],
    'era5-pressure-levels-ensemble_members': [
        'reanalysis-era5-pressure-levels',
        {
            'variable': 'temperature',
            'pressure_level': ['500', '850'],
            'product_type': 'ensemble_members',
            'year': '2017',
            'month': '01',
            'day': '01',
            'time': ['00:00', '12:00'],
            'grid': ['3', '3'],
            'format': 'grib',
        },
        192,
    ],
}


@pytest.mark.parametrize('test_file', TEST_FILES.keys())
def test_reanalysis_Stream(test_file):
    dataset, request, key_count = TEST_FILES[test_file]
    path = cdscommon.ensure_data(dataset, request, name='cds-' + test_file + '-{uuid}.grib')

    stream = eccodes_grib.Stream(path)
    leader = stream.first()
    assert len(leader) == key_count
    assert sum(1 for _ in stream) == leader['count']


@pytest.mark.parametrize('test_file', TEST_FILES.keys())
def test_reanalysis_Dataset(test_file):
    dataset, request, key_count = TEST_FILES[test_file]
    path = cdscommon.ensure_data(dataset, request, name='cds-' + test_file + '-{uuid}.grib')

    res = eccodes_grib.Dataset(path)
    assert len(res.variables) == 1
