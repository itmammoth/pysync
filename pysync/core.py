import hjson
import os
import subprocess
from pathlib import Path


def do_sync(settings_path):
    print('Start pysyncing...')

    settings = __load_json(settings_path)
    dest_root_path = __get_dest_root_path(settings['destination'])
    dest_root_path.mkdir(parents=True, exist_ok=True)

    filters = settings.get('filters', [])
    global_exclusions = settings.get('global_exclusions', [])

    for source in settings['sources']:
        rsync_args = __build_rsync_args(settings)

        # filter
        if 'filter' in source:
            rsync_args.extend(filters[source['filter']])
        # global exclusions
        for ex in global_exclusions:
            rsync_args.extend(['--exclude', ex])
        # source exclusions
        if 'exclusions' in source:
            for ex in source['exclusions']:
                rsync_args.extend(['--exclude', ex])

        source_path = Path(source['path'])
        rsync_args.append(str(source_path.resolve()))
        rsync_args.append(str(dest_root_path.resolve()))
        subprocess.call(rsync_args)

    print('Successfully pysynced!')


def __load_json(settings_path):
    with open(settings_path, 'rt') as f:
        return hjson.load(f)


def __get_dest_root_path(destination_path):
    hostname = os.uname()[1]
    return Path(destination_path) / 'pysync' / hostname


def __build_rsync_args(settings):
    options = settings.get('rsync_options')
    if not options:
        options = ['-a', '-v', '-h']
    return ['rsync'] + options
