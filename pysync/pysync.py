import json
import os
import subprocess
from pathlib import Path


def do_sync(settings_path):
    print('Start pysyncing...')

    settings = __load_json(settings_path)
    dest_root_path = __get_dest_root_path(settings['destination'])
    dest_root_path.mkdir(parents=True, exist_ok=True)

    for source in settings['sources']:
        source_path = Path(source['path'])
        rsync_args = ['rsync', '-a', '-v', '-h']
        if 'exclusions' in source:
            for exclusion in source['exclusions']:
                rsync_args.append('--exclude')
                rsync_args.append(exclusion)
        rsync_args.append(str(source_path.resolve()))
        rsync_args.append(str(dest_root_path.resolve()))
        subprocess.call(rsync_args)

    print('done.')


def __load_json(settings_path):
    with open(settings_path, 'rt') as f:
        return json.load(f)


def __get_dest_root_path(destination_path):
    hostname = os.uname()[1]
    return Path(destination_path) / 'pysync' / hostname
