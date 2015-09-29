from setuptools import setup

##########################
VERSION = "0.1"
ISRELEASED = False
__version__ = VERSION
##########################

##########################
# Setup
##########################

setup(
    name='minder',
    version=__version__,
    author='Daniel L Parton',
    author_email='',
    description='Notetaking app',
    license='',
    packages=[
        'minder',
        'cli',
    ],
    entry_points={'console_scripts':
        [
            'minder = cli.cli:main'
        ]
    },
)
