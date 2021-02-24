from libs.page import *
from tkinter import ttk
from controllers.notes import Notes


class ReminderPage(Page):
    __notes_controller = Notes()

    def __init__(self, parent):
        Page.__init__(self, parent)

        self._parent = parent
        self._draw()

    def _draw(self):
        label = Label(self._parent, text="Reminders:", bg="#201F1E", fg="lightgrey")
        label.config(font=("Courier", 18))
        label.place(x=70, y=35)

        self._drawTable()
        self._drawActions()

    def __insertToTable(self):
        for i in self._table.get_children():
            self._table.delete(i)
        notes = self.__notes_controller.getAll()
        for note in notes:
            self._table.insert("", "end", values=(note['id'], note['title'], note['time']), iid=note['id'])

    def _drawTable(self):

        style = ttk.Style(self._parent)

        self._table = ttk.Treeview(self._parent, selectmode='browse', show='headings', height=5)

        scroll = ttk.Scrollbar(self._parent, orient="vertical", command=self._table.yview)

        self._table.configure(xscrollcommand=scroll.set)

        cols = ('#ID', 'Title', 'Time')
        self._table["columns"] = cols

        for col in cols:
            self._table.column(col, anchor=CENTER, width=130)
            self._table.heading(col, text=col, anchor=CENTER)

        style.configure("Treeview.Heading", font=("Courier", 15), padding=10, foreground='red')
        style.configure("Treeview", font=("Courier", 12), rowheight=30)

        self.__insertToTable()

        self._table.pack(side='left')
        self._table.place(x=70, y=70)
        scroll.pack(side='left')
        scroll.place(x=800, y=70)

    def _drawActions(self):
        form_frame = Frame(self._parent, bg="#201F1E")
        form_frame.place(x=30, y=290)

        title_label = Label(form_frame, text="Title", width=20, bg="#201F1E", fg="lightgrey")
        title_label.config(font=("Courier", 12))
        title_label.grid(row=0, column=0)

        time_label = Label(form_frame, text="Time (24:00 format)", width=20, bg="#201F1E", fg="lightgrey")
        time_label.config(font=("Courier", 12))
        time_label.grid(row=0, column=1)

        self._title_input = Entry(form_frame)
        self._title_input.grid(row=1, column=0)

        time_frame = Frame(form_frame)
        time_frame.grid(row=1, column=1)

        self._hour_input = Entry(time_frame, width=4)
        self._hour_input.grid(row=0, column=0)

        self._min_input = Entry(time_frame, width=4)
        self._min_input.grid(row=0, column=1)

        create_note = Button(form_frame, text='Create Note', command=self._create)
        create_note.grid(row=1, column=2)

        delete_note = Button(self._parent, text='Delete Note', command=self._delete)
        delete_note.place(x=442, y=350)

        self._validation_label = Label(form_frame, bg="#201F1E", fg="red")

    def _create(self):
        title = self._title_input.get()
        hour = self._hour_input.get()
        min = self._min_input.get()

        self._validation_label.configure(text="")
        self._validation_label.config(font=("Courier", 7))
        self._validation_label.grid(row=2, column=1)

        if not (51 > len(title) > 2):
            self._validation_label.configure(text="Title should be between 2 & 50 characters")
            self._validation_label.config(font=("Courier", 7))
            self._validation_label.grid(row=2, column=0)
            return

        if not hour.isnumeric() \
                or not min.isnumeric() \
                or not (3 > len(hour) > 0) \
                or not (3 > len(hour) > 0) \
                or int(hour) > 23 \
                or int(min) > 59:
            self._validation_label.configure(text="Hour & min should be time format")
            self._validation_label.config(font=("Courier", 7))
            self._validation_label.grid(row=2, column=1)
            return

        self.__notes_controller.create(title, hour + ':' + min)

        self.__insertToTable()

        self._title_input.delete(0, END)
        self._hour_input.delete(0, END)
        self._min_input.delete(0, END)

    def _delete(self):
        self.__notes_controller.delete(self._table.selection()[0])
        self.__insertToTable()
