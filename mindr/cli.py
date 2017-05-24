from docopt import docopt
from mindr.core import MindrDB
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
  mindr stats

n <notename>       new note
t                  print tags
t <tag>            print list of notes with given tag
tv <tag>           view notes with given tag
a                  print anthologies
a <anthology>      view notes in anthology
ae <anthology>     edit anthology
stats              print mindr stats
"""

db = MindrDB()


def main():
    args = docopt(docopt_helpstring, help=True)
    if args['n']:
        db.mk_new_note(args['<notename>'])
    elif args['t']:
        if args['<tag>']:
            print_notes_by_tag(db, tag=args['<tag>'])
        else:
            print_tags(db)
    elif args['tv']:
        view_tagged_notes(db, args['<tag>'])
    elif args['notes']:
        print_notes(db)
    elif args['untagged']:
        print_untagged_notes(db)
    elif args['a']:
        if args['<anthology>']:
            open_anthology(db, args['<anthology>'])
        else:
            print_anthologies()
            print('\n'.join(anthologies))
    elif args['ae']:
        edit_anthology(db, args['<anthology>'])
    elif args['s']:
        note_stats(db)


def note_stats(db):
    print('Number of notes: {}'.format(len(db.notes)))


def print_tags(db):
    print('\n'.join(db.tags))


def print_notes_by_tag(db, tag):
    db.populate_notes_by_tag()
    print('\n'.join(db.notes_by_tag[tag]))


def print_notes(db):
    print('\n'.join(db.notes.keys()))


def print_untagged_notes(db):
    print('\n'.join([note_name for note_name in db.notes if len(db.notes[note_name]['tags']) == 0]))
