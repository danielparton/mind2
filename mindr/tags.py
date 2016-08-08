import os
from mindr.core import Mind2MetaData
from mindr.viewing import run_marked_concat

db = Mind2MetaData()


def view_tagged_notes(tag):
    db.populate_notes_by_tag()
    notes = db.notes_by_tag[tag]
    run_marked_concat(notes)

