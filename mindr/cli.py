from docopt import docopt
from mindr.core import Mind2MetaData
from mindr.anthologies import open_anthology, anthologies, edit_anthology

docopt_helpstring = """\
Usage:
  mindr n <notename>
  mindr tags
  mindr notes
  mindr untagged
  mindr a
  mindr a <anthology>
  mindr ae <anthology>

n                  new note
a                  print anthologies
a <anthology>      view notes in anthology
ae <anthology>     edit anthology
"""

db = Mind2MetaData()


def main():
    args = docopt(docopt_helpstring, help=False)
    if args['n']:
        db.mk_new_note(args['<notename>'])
    elif args['tags']:
        print_tags()
    elif args['notes']:
        print_notes()
    elif args['untagged']:
        print_untagged_notes()
    elif args['a']:
        if args['<anthology>']:
            open_anthology(args['<anthology>'])
        else:
            print('\n'.join(anthologies))
    elif args['ae']:
        edit_anthology(args['<anthology>'])


def print_tags():
    print('\n'.join(db.tags))


def print_notes():
    print('\n'.join(db.notes.keys()))


def print_untagged_notes():
    print('\n'.join([note_name for note_name in db.notes if len(db.notes[note_name]['tags']) == 0]))
