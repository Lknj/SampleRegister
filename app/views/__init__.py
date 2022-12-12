from .main import main
from flask import Flask
BLUEPRINT = (
    (main,''),
)
#创建一个初始化的蓝图的方法
def config_blieprint(app):
    for blueprint,prefix in BLUEPRINT:
        
        app.register_blueprint(blueprint,url_prefix = prefix)