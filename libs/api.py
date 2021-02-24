import requests
from models.prayer_day import PrayerDay
from models.prayer import Prayer
from datetime import datetime
from dateutil.parser import parse

_today = datetime.date(datetime.now())
_prayer_day = PrayerDay()
_prayer = Prayer()


def getIP():
    return requests.get('https://api.ipify.org').text


def insertIntoDatabase(data):
    day_data = {
        "day": _today
    }
    for key, value in data['settings']['location'].items():
        day_data[key] = value

    prayer_day_id = _prayer_day.create(day_data)

    for prayer, time in data['results'].items():
        time = parse(time.replace('%', ''))
        if prayer == "Duha":
            _prayer.create({"name": prayer, "time": time, "run_azan": 0, "prayer_day_id": prayer_day_id})
        else:
            _prayer.create({
                "name": prayer,
                "time": time,
                "run_azan": 1,
                "prayer_day_id": prayer_day_id
            })


def getAzanDataFromAPI():
    exists_one = _prayer_day.find('day', '=', _today)

    if len(exists_one) == 0:
        response = requests.get(f'http://www.islamicfinder.us/index.php/api/prayer_times?user_ip={getIP()}')
        print(response.json())
        insertIntoDatabase(response.json())


getAzanDataFromAPI()
