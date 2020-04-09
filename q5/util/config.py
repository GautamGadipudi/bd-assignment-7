from configparser import ConfigParser

from util.constants import PG_CONNECTION_CONFIG_FILE_PATH, PG_CONNECTION_CONFIG_SECTION


def get_connection_config(filename=PG_CONNECTION_CONFIG_FILE_PATH, section=PG_CONNECTION_CONFIG_SECTION):
    parser = ConfigParser()
    parser.read(filename)

    db = {}

    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in the file {filename}')
    return db