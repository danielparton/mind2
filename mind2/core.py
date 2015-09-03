import os


class Mind2MetaData(object):
    def __init__(self):
        self.project_dir = '.'
        self.get_note_filepaths()
        self.get_metadata()

    def get_note_filepaths(self):
        self.note_filepaths = [
            filepath for filepath in os.listdir(self.project_dir)
            if (len(filepath) > 4 and filepath[-4:] == '.txt')
        ]

    def get_metadata(self):
        notes = {}
        tags = set()
        for note_filepath in self.note_filepaths:
            note_name = note_filepath[: note_filepath.index('.txt')]
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
