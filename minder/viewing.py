import os
from minder.core import Mind2MetaData, dotfile, notes_dirpath
from subprocess import Popen

mind2metadata = Mind2MetaData()

def run_viewer(note_names):
    note_filepaths = [os.path.join(notes_dirpath, note_name) + '.txt' for note_name in note_names]
    Popen(
        [
            dotfile.viewer_path,
        ] + note_filepaths
    )
