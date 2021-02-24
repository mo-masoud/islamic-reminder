from libs.sidebar.image import *
from libs.sidebar.scrollbar import *

side_bar_tab_list = []


class SideBar(ScrollBar):
    def __init__(self, parent):
        ScrollBar.__init__(self, parent)
        self.color = "#232323"

    def finish(self):
        self.select_first_tab()
        if len(scroll_on_items_list) < 14:
            i = len(scroll_on_items_list)
            index = 14 - i
            for i in range(index):
                Spacer(self.scrollframe, "")

    def add_spacer(self, text):
        Spacer(self.scrollframe, text)

    def add_button(self, text, command, icon=None, tab=True):
        SideBarButton(self.scrollframe, text, command, icon=icon, tab=tab)

    def select_first_tab(self):
        i = side_bar_tab_list[0]
        i.click()


class Spacer(Canvas):
    def __init__(self, parent, text, *args, **kwargs):
        self.frame_color = "#232323"
        self.hover_border_color = "grey"

        Canvas.__init__(self, parent, width=199, height=35, bg=self.frame_color, highlightthickness=1,
                        highlightbackground=self.frame_color, *args, **kwargs)
        self.pack()

        self.text = Label(self, text=text, bg=self.frame_color, font="Segoe 10 bold", fg="lightgrey")
        self.text.place(x=3, y=12)

        scroll_on_items_list.append(self)

    def hover(self, event=None):
        self.config(highlightbackground=self.hover_border_color)

    def unHover(self, event=None):
        self.config(highlightbackground=self.frame_color)

    def click(self, event=None):
        print()


class SideBarButton(Canvas):
    def __init__(self, parent, text, command, icon=None, tab=True, *args, **kwargs):

        self.frame_color = "#232323"
        self.hover_color = "#4D4c4c"
        self.hover_border_color = "grey"
        self.is_tab = tab

        self.selected = False

        self.command = command

        Canvas.__init__(self, parent, width=198, height=35, bg=self.frame_color, highlightthickness=1,
                        highlightbackground=self.frame_color, *args, **kwargs)
        self.pack()

        if icon is None:
            pass
        else:
            self.icon = sprite(icon, 20, 20)
            self.create_image(20, 20, image=self.icon)

        self.text = Label(self, text=text, font="Segoe 10", bg=self.frame_color, fg="lightgrey")
        self.text.place(x=40, y=10)

        self.bind('<Enter>', self.hover)
        self.bind('<Button-1>', self.click)
        if self.is_tab is False:
            self.bind('<ButtonRelease-1>', self.unClick)

        self.text.bind('<Enter>', self.hover)
        self.text.bind('<Button-1>', self.click)
        if self.is_tab is False:
            self.text.bind('<ButtonRelease-1>', self.unClick)
        if self.is_tab:
            side_bar_tab_list.append(self)
        scroll_on_items_list.append(self)

    def hover(self, event=None):
        if self.selected is False:
            self.bind('<Leave>', self.unHover)
            self.config(highlightbackground=self.hover_border_color, bg=self.hover_color)
            self.text.config(bg=self.hover_color)

    def unHover(self, event=None):
        self.config(highlightbackground=self.frame_color, bg=self.frame_color)
        self.text.config(bg=self.frame_color)

    def click(self, event=None):

        if self.is_tab:
            self.bind('<Leave>', str)
            for i in side_bar_tab_list:
                i.unHover()
                i.selected = False

        self.selected = True

        self.config(bg=self.hover_border_color)
        self.text.config(bg=self.hover_border_color)

        self.command()

    def unClick(self, event=None):
        self.selected = False
        self.config(bg=self.hover_color)
        self.text.config(bg=self.hover_color)
