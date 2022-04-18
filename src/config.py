from distutils.log import Log
from pathlib import Path
from time import pthread_getcpuclockid

BASE_PATH = Path.cwd().absolute()
DATA_PATH = Path.joinpath(BASE_PATH, 'data')
LOG_PATH = Path.joinpath(BASE_PATH, 'logs')
SAMPLE_FILE_PATH = Path.joinpath(BASE_PATH, 'sample_data', 'sample.osm')

OSM_FILE_NAME = 'map.osm'

LOG_FILE_PATH = Path.joinpath(LOG_PATH, 'log')
