from libs.model import Model


class Prayer(Model):

    _fillable = {
        "prayer_day_id": "INTEGER",
        "name": "VARCAHR(20)",
        "time": "TIMESTAMP",
        "run_azan": "TINYINT(1) DEFAULT 1",
    }
    _timestamp = True

    _fillable_references = {
        "prayer_day_id": "prayer_days(id)"
    }

    def __init__(self):
        Model.__init__(self, "prayers")