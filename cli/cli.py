from docopt import docopt
from mind2.core import Mind2MetaData

docopt_helpstring = """\
Usage:
  mind2 tags
  mind2 notes
  mind2 untagged
"""

db = Mind2MetaData()


def main():
    args = docopt(docopt_helpstring, help=False)
    if args['tags']:
        print_tags()
    elif args['notes']:
        print_notes()
    elif args['untagged']:
        print_untagged_notes()


def print_tags():
    print('\n'.join(db.tags))


def print_notes():
    print('\n'.join(db.notes.keys()))


def print_untagged_notes():
    print('\n'.join([note_name for note_name in db.notes if len(db.notes[note_name]['tags']) == 0]))

