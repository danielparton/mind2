from docopt import docopt
from mindr.core import Mind2MetaData
from mindr.anthologies import open_anthology, anthologies, edit_anthology
from mindr.tags import view_tagged_notes

docopt_helpstring = """\
Usage:
  mindr n <notename>
  mindr t
  mindr t <tag>
  mindr tv <tag>
  mindr notes
  mindr untagged
  mindr a
  mindr a <anthology>
  mindr ae <anthology>

n                  new note
t                  print tags
t <tag>            print list of notes with tag
tv <tag>           view notes with tag
a                  print anthologies
a <anthology>      view notes in anthology
ae <anthology>     edit anthology
"""

db = Mind2MetaData()


def main():
    args = docopt(docopt_helpstring, help=False)
    if args['n']:
        db.mk_new_note(args['<notename>'])
    elif args['t']:
        if args['<tag>']:
            db.populate_notes_by_tag()
            print('\n'.join(db.notes_by_tag[args['<tag>']]))
        else:
            print_tags()
    elif args['tv']:
        view_tagged_notes(tag)
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
