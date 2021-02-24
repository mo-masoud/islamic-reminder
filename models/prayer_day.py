from libs.model import Model


class PrayerDay(Model):

    _fillable = {"city": "VARCAHR(50)", "state": "VARCAHR(50)", "country": "VARCHAR(50)", "day": "DATE"}
    _timestamp = True
    _fillable_references = {}

    def __init__(self):
        Model.__init__(self, "prayer_days")