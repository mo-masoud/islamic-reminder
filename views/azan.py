from libs.page import *
from tkinter import ttk
from controllers.azan import Azan as AzanController


class AzanPage(Page):
    _parent = None
    _controller = AzanController()

    def __init__(self, parent):
        Page.__init__(self, parent)

        self._parent = parent
        self._draw()

    def _draw(self):

        data = self._controller.getAll()

        label = Label(self._parent, text="Prayers Times:", bg="#201F1E", fg="lightgrey")
        label.config(font=("Courier", 18))
        label.place(x=70, y=35)

        self._drawTable(data['prayers'])

        text = f"{data['today']['country']} - {data['today']['state']} - {data['today']['city']} ({data['today']['day']})"
        label = Label(self._parent, text=text, bg="#201F1E", fg="lightgrey")
        label.config(font=("Courier", 11))
        label.place(x=70, y=300)

    def _drawTable(self, prayers):
        style = ttk.Style(self._parent)

        cols = ('Prayer Name', 'Time')
        table = ttk.Treeview(self._parent, columns=cols, show='headings', height=6)
        table['column'] = cols

        for col in cols:
            table.column(col, anchor=CENTER)
            table.heading(col, text=col, anchor=CENTER)

        style.configure("Treeview.Heading", font=("Courier", 15), padding=10, foreground='red')
        style.configure("Treeview", font=("Courier", 12), rowheight=30)

        for prayer in prayers:
            table.insert("", "end", values=("   " + prayer['name'], "     " + prayer['time']))

        table.place(x=70, y=70)
