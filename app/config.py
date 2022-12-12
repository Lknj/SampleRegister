class Config:
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mysql@localhost:3306/database_name'

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mysql@localhost:3306/database_name'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mysql@localhost:3306/database_name'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    "production": DevelopmentConfig,
    "default": DevelopmentConfig
}