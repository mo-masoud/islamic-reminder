from models.note import Note
from datetime import datetime
from dateutil.parser import parse


class Notes:
    __note = Note()
    __today = datetime.date(datetime.now())

    def getAll(self, order_by='id', order_method='DESC'):
        notes_data = self.__note.find('id', '>', '0', order_by, order_method)
        notes = []

        for note in notes_data:
            if parse(note['time']).date() == self.__today:
                note['time'] = datetime.strptime(note['time'], "%Y-%j-%d %H:%M:%S").strftime('%I:%M %p')
                notes.append(note)

        return notes

    def create(self, title, time):
        time = parse(time)
        note = {
            'title': title,
            'time': time,
        }
        id = self.__note.create(note)
        note['id'] = id
        from libs.alarm import notes
        notes.append(note)

    def delete(self, id):
        self.__note.delete({'key': 'id', 'value': id})
        from libs.alarm import notes
        for i in range(len(notes)):
            if notes[i]['id'] == int(id):
                del notes[i]
                break
