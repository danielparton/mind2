import os
from mindr.core import Mind2MetaData
from subprocess import Popen

db = Mind2MetaData()
notes_dirpath = db.notes_dirpath
viewer_path = db.config.viewer_path

def run_viewer(note_names):
    note_filepaths = [os.path.join(notes_dirpath, note_name) + '.txt' for note_name in note_names]
    Popen(
        [
            viewer_path,
        ] + note_filepaths
    )
