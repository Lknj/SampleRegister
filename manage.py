import os
from flask_script import Server,Manager
from flask_migrate import MigrateCommand
from app import strat_app
config_name = os.environ.get('FLASK_CONFIG') or 'default'
app = strat_app(config_name)

manage = Manager(app)
manage.add_command("runserver", Server(use_debugger=True))
manage.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manage.run()