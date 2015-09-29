from minder.core import Mind2MetaData
from subprocess import Popen

mind2metadata = Mind2MetaData()

viewer_path = '/Applications/Marked 2.app/Contents/MacOS/Marked 2'

def run_viewer(note_names):
    Popen(
        [
            viewer_path,
        ] + mind2metadata.note_filepaths
    )

if __name__ == '__main__':
    run_viewer(note_names)


