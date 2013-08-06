import argparse
import sys

import mongo_migrate

def create_parser(prog_name):
    def get_version():
        return mongo_migrate.get_version()

    def usage():
        return "%(prog)s [options] direction target"

    parser = argparse.ArgumentParser(prog=prog_name,
            usage=usage(),
            description='mongo_migrate')
    parser.add_argument('-H', '--host', action='store', nargs='?', default='localhost', 
            type=str, required=True, metavar='HOST', dest='host')
    parser.add_argument('-P', '--port', action='store', nargs='?', default=27017, 
            type=int, required=True, metavar='PORT', dest='port')
    parser.add_argument('-d', '--database', action='store', nargs='?', 
            type=str, required=True, metavar='DATABASE', dest='database')
    parser.add_argument('-l', '--location', action='store', nargs='?', default='./migrations',
            type=str, required=True, metavar='LOCATION', dest='location')
    parser.add_argument('direction', action='store', default='up',
            type=str, choices=['up', 'down'], metavar='DIRECTION')
    parser.add_argument('target', action='store',
            type=str,  metavar='TARGET')

    return parser




if __name__ == '__main__':
    parser = create_parser(sys.argv[0])
    print parser.print_help()
    args = parser.parse_args(sys.argv[1:])
    print args
    print args.database
    print args.host
