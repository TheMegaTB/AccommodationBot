import json
import os.path

from conf import configuration
cache_config = configuration['cache']


def save(values):
    json_string = json.dumps(values)
    f = open(cache_config['file'], "w")
    f.write(json_string)
    f.close()


def load():
    if not os.path.isfile(cache_config['file']):
        return cache_config['defaults']

    f = open(cache_config['file'])
    json_string = f.read()
    f.close()
    values = json.loads(json_string)
    return values
