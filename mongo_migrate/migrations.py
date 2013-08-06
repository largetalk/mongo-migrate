#coding=utf8
from mongo_migrate.configs import MongoConfig

class Migrator(object):
    def __init__(self, migration_js, fake=False):
        self.migration_js = migration_js
        self._fake = fake

    def up(self):
        pass

    def down(self):
        pass

    def _effect_db(self, direction):
        pass


class Migrations(object):
    def __init__(self, js_folder):
        self.js_folder = js_folder

    def up(self, target):
        pass

    def down(self, target):
        pass
