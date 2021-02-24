from libs.model import Model


class Note(Model):

    _fillable = {
        "title": "VARCAHR(50)",
        "time": "TIMESTAMP",
    }
    _timestamp = True

    _fillable_references = {
    }

    def __init__(self):
        Model.__init__(self, "notes")