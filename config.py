class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_KEY = '96573ce4e2984891a9f56fd982912bc8'

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    '''
    Pruduction  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    NEWS_API_KEY = '96573ce4e2984891a9f56fd982912bc8'
    pass


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    NEWS_API_KEY = '96573ce4e2984891a9f56fd982912bc8'
    DEBUG = True


class TestConfig(Config):
    '''
    Test  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
