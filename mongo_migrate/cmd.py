from mongo_migrate.configs import MongoConfig
from mongo_migrate.migrations import Migrator
from pymongo import MongoClient
import os

class BaseCommand(object):
    def __init__(self, args):
        self.js_path = args.location
        self.db = MongoClient(MongoConfig.host, MongoClient.port)[MongoConfig.db]
        self.his_collect = self.db[MongoConfig.his_collect]

    @property
    def applied(self):
        if not hasattr(self, '_applied'):
            self._applied = []
            cursor = self.his_collect.find({}, {'migration'})
            for it in cursor:
                self._applied.append(it['migration'])
        return sorted(self._applied)

    @property
    def unapplied(self):
        all_js = sorted([ x for x in os.listdir(self.js_path) if os.path.isfile(os.path.join(self.js_path, x)) and x.endswith('.js') ])
        return sorted([ x for x in all_js if x not in self.applied])
    
    def execute(self):
        raise NotImplementedError

class MigrateCommand(BaseCommand):
    def __init__(self, args):
        self.direction = True if args.cmd == 'up' else False
        super(MigrateCommand, self).__init__(args)

    def execute(self):
        for js in self.unapplied:
            migrator = Migrator(self, os.path.join(self.js_path, js))
            migrator.up()

        delattr(self, '_applied')
            

class ListCommand(BaseCommand):
    def execute(self):
        print 'this is ListCommand execute'
