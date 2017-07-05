import ConfigParser

Config = ConfigParser.ConfigParser()
Config.read('config.ini')

def parse_config_file(section):
    """Parse config.ini file with DB access

    :return:
    options for connect with DB
    """

    db_parameters = {}

    if Config.has_section(section):
        options = Config.options(section)
        for option in options:
            db_parameters[option] = Config.get(section, option)
    return db_parameters
