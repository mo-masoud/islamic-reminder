from models.prayer_day import PrayerDay
from models.prayer import Prayer
from datetime import datetime


class Azan:
    _prayer_day = PrayerDay()
    _prayer = Prayer()
    _today = datetime.date(datetime.now())

    def getAll(self):
        today = self._prayer_day.find('day', '=', self._today)[0]
        prayers_data = self._prayer.find('prayer_day_id', '=', today['id'])
        prayers = []

        for prayer in prayers_data:
            prayer['time'] = datetime.strptime(prayer['time'], "%Y-%j-%d %H:%M:%S").strftime('%I:%M %p')
            prayers.append(prayer)

        data = {
            "today": today,
            "prayers": prayers
        }

        return data
