from pathlib import Path

from osgeo import gdal

sample_data = Path(__file__).parent / '../sample_data'


def test_driver():
    formats = [gdal.GetDriver(i).LongName.lower() for i in range(gdal.GetDriverCount())]
    assert any(['mrsid' in f for f in formats])


def test_open(filename='mercator.sid'):
    path = sample_data / filename
    if not path.is_file():
        raise Exception(f'{path} not found')
    ds = gdal.Open(str(path))
    assert ds.RasterXSize == 515
