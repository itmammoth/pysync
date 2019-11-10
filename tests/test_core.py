import os
import shutil
from pathlib import Path
from pysync import do_sync


DEST_PATH = Path('tests/dest/pysync')


def setup_module(module):
    shutil.rmtree(DEST_PATH, ignore_errors=True)


def test_do_pysync():
    do_sync(settings_path='tests/pysync_test.json')

    hostname = os.uname()[1]
    assert (DEST_PATH / hostname).exists()

    BACK_ME_UP1 = DEST_PATH / hostname / 'BackMeUp1'
    assert BACK_ME_UP1.exists()
    assert (BACK_ME_UP1 / 'file1.txt').exists()
    assert (BACK_ME_UP1 / 'file2.txt').exists()
    assert not (BACK_ME_UP1 / '.DS_Store').exists()
    assert not (BACK_ME_UP1 / 'x.log').exists()
    assert not (BACK_ME_UP1 / 'tmp').exists()

    BACK_ME_UP2 = DEST_PATH / hostname / 'BackMeUp2'
    assert BACK_ME_UP2.exists()
    assert (BACK_ME_UP2 / 'file3.txt').exists()
    assert not (BACK_ME_UP2 / '.DS_Store').exists()
    assert not (BACK_ME_UP2 / '.git').exists()
    assert not (BACK_ME_UP2 / 'ignore_me').exists()

    assert not (DEST_PATH / 'X').exists()
