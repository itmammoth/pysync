def main():
    import argparse
    from .core import do_sync
    from . import __version__
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config-file', help='indicate config file path')
    parser.add_argument('--version', action='version', version=__version__)
    args = parser.parse_args()
    config_path = __resolve_config_file_path(args.config_file, '~/.config/pysync.json', '~/pysync.json')
    do_sync(config_path)


def __resolve_config_file_path(path, *defaults):
    from pathlib import Path
    if path:
        expanded_path = Path(path).expanduser()
        if expanded_path.exists():
            return str(expanded_path.resolve())
        raise Exception('Not found config file `{}`'.format(path))
    for default_path in defaults:
        expanded_path = Path(default_path).expanduser()
        if expanded_path.exists():
            return str(expanded_path.resolve())
    raise Exception("Not found config file in [{}]".format(', '.join(defaults)))


if __name__ == '__main__':
    main()
