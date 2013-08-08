from __future__ import print_function
import argparse
import sys
import traceback

import mongo_migrate
from mongo_migrate.cmd import UpMigrateCommand
from mongo_migrate.cmd import DownMigrateCommand
from mongo_migrate.cmd import ListCommand

class Argument(object):
    def __init__(self):
        pass

    def get_version(self):
        return mongo_migrate.get_version()
    
    def usage(self):
        return "%(prog)s [options] cmd"

    def create_parser(self, prog_name):
        self.parser = argparse.ArgumentParser(prog=prog_name,
                usage=self.usage(),
                description='mongo_migrate')
        self.parser.add_argument('-H', '--host', action='store', nargs='?', default='localhost', 
                type=str, required=True, metavar='HOST', dest='host')
        self.parser.add_argument('-P', '--port', action='store', nargs='?', default=27017, 
                type=int, required=True, metavar='PORT', dest='port')
        self.parser.add_argument('-d', '--database', action='store', nargs='?', 
                type=str, required=True, metavar='DATABASE', dest='database')
        self.parser.add_argument('-l', '--location', action='store', nargs='?', default='./migrations',
                type=str, required=True, metavar='LOCATION', dest='location')

        self.parser.add_argument('cmd', action='store', default='up',
                type=str, choices=['up', 'down', 'list'], metavar='cmd')
        #self.parser.add_argument('target', action='store', default='123',
        #        type=str,  metavar='TARGET')

        return self.parser

    def init_mongo_config(self, args):
        from mongo_migrate.configs import MongoConfig
        MongoConfig.host = args.host
        MongoConfig.port = args.port
        MongoConfig.db = args.database

    def cmd_factory(self, args):
        cmd_mapping = {
            'up': 'UpMigrateCommand',
            'down': 'DownMigrateCommand',
            'list': 'ListCommand',
        }
        return eval(cmd_mapping[args.cmd])(args)

    def execute_from_argv(self, argv):
        parser = self.create_parser(argv[0])
        args = parser.parse_args(argv[1:])

        self.init_mongo_config(args)
        self.cmd = self.cmd_factory(args)
        self.execute()
    
    def execute(self):
        try:
            self.cmd.execute()
        except BaseException as e:
            stderr = sys.stderr
            if True: # debug
                stderr.write(traceback.format_exc())
            else:
                stderr.write('%s: %s' % (e.__class__.__name__, e))
            sys.exit(1)

def execute_from_command_line():
    argument = Argument()
    argument.execute_from_argv(sys.argv)

if __name__ == '__main__':
    parser = Argument().create_parser(sys.argv[0])
    parser.print_help()
    args = parser.parse_args(sys.argv[1:])
    print(args)
    print(args.database)
    print(args.host)
    print(args.port, type(args.port))
