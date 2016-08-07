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
    name='mindr',
    version=__version__,
    author='Daniel L Parton',
    author_email='',
    description='Notetaking app',
    license='',
    packages=[
        'mindr',
    ],
    entry_points={'console_scripts':
        [
            'mindr = mindr.cli:main'
        ]
    },
)
