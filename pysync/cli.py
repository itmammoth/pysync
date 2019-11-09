def main():
    import argparse
    from .core import do_sync
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--settings-file', help='Indicate settings json path')
    args = parser.parse_args()
    settings_file = args.settings_file or 'settings.json'
    do_sync(settings_file)


if __name__ == '__main__':
    main()
