import threading
import time
from datetime import datetime
from controllers.notes import Notes
from controllers.azan import Azan
from dateutil.parser import parse
from playsound import playsound
from win10toast import ToastNotifier

notes = Notes().getAll()
prayers = Azan().getAll()


def __ring__(title, ring_type='reminder'):
    notify = ToastNotifier()
    notify.show_toast(str(title), "It's time!", icon_path='assets/images/icon.ico', duration=10, threaded=True)

    if ring_type == 'reminder':
        playsound('assets/sounds/reminder.mp3')
    else:
        playsound('assets/sounds/azan.mp3')


def __alarm__():
    while True:
        time_now = parse(str(datetime.now())).time().strftime('%H:%M')
        for note in notes:
            t = parse(str(note['time'])).time().strftime('%H:%M')
            if t == time_now:
                __ring__(note['title'])

        for prayer in prayers['prayers']:
            t = parse(str(prayer['time'])).time().strftime('%H:%M')
            if t == time_now:
                if prayer['run_azan'] == 1:
                    __ring__(prayer['name'], 'azan')
                else:
                    __ring__(prayer['name'])

        time.sleep(60)


def start_alarm():
    t = threading.Thread(target=__alarm__)
    t.daemon = True
    t.start()
