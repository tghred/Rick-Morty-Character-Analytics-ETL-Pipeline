from configparser import ConfigParser

def config(filename='../config/database.ini', section='postgresql'):
    parser = ConfigParser()

    if not parser.read(filename):
        raise IOError('Unable to read configuration file')
    db = {}
    if parser.has_section(section):
        prams = parser.items(section)
        for param in prams:
            db[param[0]] = param[1]
    else:
        raise IOError(f"Section '{section}' not found. Please check the configuration file.")
