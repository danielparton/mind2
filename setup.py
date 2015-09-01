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
    name='mind2',
    version=__version__,
    author='Daniel L Parton',
    author_email='',
    description='Notetaking app',
    license='',
    packages=[
        'mind2',
        'cli',
    ],
    entry_points={'console_scripts':
        [
            'mind2 = cli.cli:main'
        ]
    },
)
