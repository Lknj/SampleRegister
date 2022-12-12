from flask import Flask, render_template
from app.views import config_blieprint
from app.config import config
from app.extensions import config_extension

#创建一个初始化Flask项目的方法
def strat_app(config_name):
    app = Flask(config_name)
    app.config.from_object(config[config_name] or config['default'])
    config[config_name].init_app(app)
    config_extension(app)
    config_blieprint(app)
    config_errorhandler(app)
    return app
#定制404页面
def config_errorhandler(app):
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html')