import ast
import re
import os

from setuptools import setup

PACKAGE_NAME = 'pysync'

with open(os.path.join(PACKAGE_NAME, '__init__.py')) as f:
    match = re.search(r'__version__\s+=\s+(.*)', f.read())
version = str(ast.literal_eval(match.group(1)))

setup(
    # metadata
    name='itm.pysync',
    version=version,
    url='https://github.com/itmammoth/pysync',
    author='itmammoth',
    author_email='itmammoth@gmail.com',
    maintainer='itmammoth',
    maintainer_email='itmammoth@gmail.com',
    description='A simple backup/sync tool with rsync',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',

    # options
    packages=[PACKAGE_NAME],
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.5',
    install_requires=open('requirements.txt').read().splitlines(),
    extras_require={
        'dev': [
            'pytest>=5'
        ],
    },
    entry_points='''
        [console_scripts]
        {app}={pkg}.cli:main
    '''.format(app=PACKAGE_NAME.replace('_', '-'), pkg=PACKAGE_NAME),
)
