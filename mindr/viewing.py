import os
from mindr.core import Mind2MetaData
from subprocess import Popen
import subprocess

db = Mind2MetaData()
notes_dirpath = db.notes_dirpath
viewer_path = db.config.viewer_path


def run_viewer(note_names):
    note_filepaths = [os.path.join(notes_dirpath, note_name) + '.txt' for note_name in note_names]
    subprocess.check_output(viewer_path + ' ' + ' '.join(note_filepaths), shell=True)


def run_marked_concat(note_names):
    note_filepaths = [os.path.join(notes_dirpath, note_name) + '.txt' for note_name in note_names]
    subprocess.check_output("""awk 'FNR==1{{print "\\n---\\n"}}1' {} | open -f -a Marked\ 2""".format(' '.join(['"{}"'.format(x) for x in note_filepaths])), shell=True)


def run_marked(note_names):
    note_filepaths = [os.path.join(notes_dirpath, note_name) + '.txt' for note_name in note_names]
    subprocess.check_output('open -a Marked\\ 2 ' + ' '.join(['"{}"'.format(x) for x in note_filepaths]), shell=True)


def run_gvim(note_names):
    note_filepaths = [os.path.join(notes_dirpath, note_name) + '.txt' for note_name in note_names]
    Popen(
        [
            viewer_path, '-p',
        ] + note_filepaths
    )
