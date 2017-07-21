import os
from flask_script import Manager, Command
from app import create_app
from instance.seed import seed_parts


app = create_app(config_name=os.getenv('APP_SETTINGS'))
manager = Manager(app)


class Seed(Command):

    def run(self):
        return seed_parts()

manager.add_command('seed', Seed())

if __name__ == '__main__':
    manager.run()
