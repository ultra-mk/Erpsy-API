import os


class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    MONGO_DB = 'erpsy'
    MONGO_URI = 'mongodb://localhost:27017/erpsy'


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True


class TestingConfig(Config):
    """Configurations for Testing."""
    TESTING = True
    MONGO_DB = 'test'
    DEBUG = True


class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
