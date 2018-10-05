from os.path import abspath, dirname, exists
from configparser import ConfigParser, ExtendedInterpolation

# docs at https://docs.python.org/3/library/configparser.html

CONFIGS = {
    uid: '{}/{}'.format(dirname(abspath(__file__)), file_name)
    for uid, file_name in dict(
        API='config_api.ini',
        GUI='config_gui.ini'
    ).items()
}


def get_config(config_uid):
    """Function returns one of the configs
    :param config_uid: API, GUI, ENV value to read selected config
    :return: config

    """
    if not exists(CONFIGS[config_uid]):
        raise AssertionError('Configuration file does n\'t exists: {}'
                             .format(CONFIGS[config_uid]))
    config = ConfigParser(interpolation=ExtendedInterpolation(), allow_no_value=True)
    config.read(CONFIGS[config_uid])
    return config


config_gui = get_config('GUI')
