VERSION = (0, 1, 0, 'alpha', 0)

def get_version(*args, **kwargs):
    from mongo_migrate.version import get_version
    return get_version(*args, **kwargs)

from mongo_migrate.argparse_compact import execute_from_command_line
