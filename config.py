from configparser import ConfigParser

def config(filename='db.ini', section='postgresql'):
    parser = ConfigParser()
    if not parser.read(filename):
        raise FileNotFoundError(filename)
    db={}
    if parser.has_section(section):
        params = parser.items(section)
        required_prams = ['host','database','user','password','port']
        for param in required_prams:
            if param not in [p[0] for p in params]:
                raise ValueError(f'Required parameter {param} is not present in {section} file')

        for param in params:
            db[pram[0]] = param[1] #assign each element in database.ini in the dict
    else:
        raise Exception(f'Section {section} not found in the {filename} file')
    return db

