##Conffiguracion molde para la aplicacion
class BaseConfig(object):
    'Base configuracion'
    SECRET_KEY = 'Key'
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://postgres:postgress@localhost:5432/base2"
class ProductionConfig(BaseConfig):
    'Produccion configuracion'
    DEBUG = False
    
class DevelopmentConfig(BaseConfig):
    'Desarrollo configuracion'
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'Desarrollo key'