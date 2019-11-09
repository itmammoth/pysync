import argparse
from pysync import pysync


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--settings-file', help='Indicate settings json path')
    args = parser.parse_args()
    settings_file = args.settings_file or 'settings.json'
    pysync.do_sync(settings_file)


if __name__ == '__main__':
    main()
