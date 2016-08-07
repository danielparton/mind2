import os
from mindr.core import Mind2MetaData
from mindr.viewing import run_viewer, run_marked, run_marked_concat
import subprocess

db = Mind2MetaData()

anthologies_dirpath = db.anthologies_dirpath
anthologies_names = os.listdir(anthologies_dirpath)

anthologies = {}

for anthology_name in anthologies_names:
    anthology_filepath = os.path.join(anthologies_dirpath, anthology_name)
    with open(anthology_filepath) as anthology_file:
        note_names = [
            name for name in anthology_file.read().splitlines() if len(name) > 0 and name[0] != '#'
        ]
    anthologies[anthology_name] = note_names


def open_anthology(anthology_name):
    note_names = anthologies[anthology_name]
    run_marked_concat(note_names)


def edit_anthology(anthology_name):
    fpath = os.path.join(db.anthologies_dirpath, anthology_name)
    subprocess.check_output('{} {} >/dev/tty'.format(db.config.editor_path, fpath), shell=True)
