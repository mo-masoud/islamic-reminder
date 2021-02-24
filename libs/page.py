from tkinter import *

active_page = []


class Page(Frame):
    def __init__(self, parent):
        self.width = 900
        self.height = 600
        try:
            active_page[0].delete()
        except:
            pass

        Frame.__init__(self, parent, bg="#201F1E", height=self.height, width=self.width)

        self.place(x=0, y=0)

        active_page.append(self)

    def delete(self):
        global active_page
        active_page.remove(self)
        self.destroy()
