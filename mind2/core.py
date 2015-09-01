import os


class Mind2MetaData(object):
    def __init__(self):
        self.project_dir = '.'
        self.get_note_filepaths()
        self.get_metadata()

    def get_note_filepaths(self):
        self.note_filepaths = [
            filepath for filepath in os.listdir(self.project_dir)
            if len(filepath) > 3 and filepath[-3:] == '.md'
        ]

    def get_metadata(self):
        notes = {}
        tags = set()
        for note_filepath in self.note_filepaths:
            note_name = note_filepath[: note_filepath.index('.md')]
            notes.update({note_name: {}})
            with open(note_filepath) as note_file:
                for line in note_file:
                    if len(line) >= 6 and line[0:6] == '@tags:':
                        note_tags = line[6:].strip().split(',')
                        break
                tags.update(note_tags)
                notes[note_name].update({'tags': note_tags})

        self.notes = notes
        self.tags = tags
