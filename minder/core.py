import os
import yaml


class DotFile(object):
    def __init__(self):
        self.dot_filename = '.minder'
        user_home_dir = os.path.expanduser('~')
        self.dot_filepath = os.path.join(user_home_dir, self.dot_filename)
        with open(self.dot_filepath) as dot_file:
            dotfile_data = yaml.load(dot_file)
        self.project_dir = dotfile_data.get('project_dir')


dotfile = DotFile()


class Mind2MetaData(object):
    def __init__(self):
        self.get_note_filepaths()
        self.get_metadata()

    def get_note_filepaths(self):
        self.note_filepaths = [
            os.path.join(dotfile.project_dir, filename) for filename in os.listdir(dotfile.project_dir)
            if (len(filename) > 4 and filename[-4:] == '.txt')
        ]

    def get_metadata(self):
        notes = {}
        tags = set()
        for note_filepath in self.note_filepaths:
            note_filename = os.path.basename(note_filepath)
            note_name = note_filename[: note_filename.index('.txt')]
            notes.update({note_name: {}})
            note_tags = []

            with open(note_filepath) as note_file:
                for line in note_file:
                    if len(line) >= 5 and line[0:5] == '@tag:':
                        note_tags.append(line[5:].strip())

            tags.update(note_tags)
            notes[note_name].update({'tags': note_tags})

        self.notes = notes
        self.tags = tags

