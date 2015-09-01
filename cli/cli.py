from docopt import docopt
from mind2.core import Mind2MetaData

docopt_helpstring = """\
Usage:
  mind2 tags
  mind2 notes
"""


def main():
    args = docopt(docopt_helpstring, help=False)
    if args['tags']:
        print_tags()
    elif args['notes']:
        print_notes()


def print_tags():
    db = Mind2MetaData()
    print('\n'.join(db.tags))


def print_notes():
    db = Mind2MetaData()
    print('\n'.join(db.notes.keys()))
