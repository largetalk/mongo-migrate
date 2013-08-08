#coding=utf8
from __future__ import print_function
from mongo_migrate.configs import MongoConfig
import subprocess
import os, sys

class Migrator(object):
    def __init__(self, cmd_obj, migration_js, fake=False):
        self.cmd_obj = cmd_obj
        self.migration_js = migration_js
        self._fake = fake

    def up(self):
        print('migrating %s' % migration_js)
        command = u'mongo {host}:{port}/{db} --eval "target=\'{target}\'" \'{file}\''.format(**{'host': MongoConfig.host,
            'port': MongoConfig.port,
            'db': MongoConfig.db,
            'target': 'up',
            'file': self.migration_js})
        try:
            subprocess.check_output(command.encode('utf-8'), shell=True)
            self._effect_db('up')
        except subprocess.CalledProcessError, e:
            sys.stderr.write('%s %s %s' % (e.cmd, e.returncode, e.output))
            raise e

    def down(self):
        pass

    def _effect_db(self, direction):
        if direction == 'up':
            self.cmd_obj.his_collect.insert({'migration': os.path.basename(self.migration_js)})
        else:
            pass


