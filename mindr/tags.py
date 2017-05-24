from mindr.viewing import run_marked_concat


def view_tagged_notes(db, tag):
    db.populate_notes_by_tag()
    notes = db.notes_by_tag[tag]
    run_marked_concat(notes)
