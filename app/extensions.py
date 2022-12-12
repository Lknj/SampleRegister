from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate


#创建对象
moment = Moment()
db = SQLAlchemy()
bootstrp = Bootstrap()
migrate = Migrate()

#创造一个初始化的方法
def config_extension(app):
    moment.init_app(app)
    db.init_app(app)
    bootstrp.init_app(app)
    migrate.init_app(app)
