from libs.sidebar.sidebar import *
from views.azan import *
from views.reminder import *
from libs.api import getAzanDataFromAPI
import libs.alarm as alarm


def main():

    getAzanDataFromAPI()

    alarm.start_alarm()

    root = Tk()
    root.resizable(False, False)
    root.title("Islamic Reminder")
    root.iconbitmap('assets/images/icon.ico')
    root.geometry("750x510")
    main_frame = Frame(root, bg="grey", width=1000, height=1000)
    main_frame.place(x=200, y=0)

    sidebar = SideBar(root)
    sidebar.add_button("Azan", lambda: AzanPage(main_frame), icon="assets/images/azan.png")
    sidebar.add_button("Reminder", lambda: ReminderPage(main_frame), icon="assets/images/notes.png")
    sidebar.finish()

    root.mainloop()


if __name__ == '__main__':
    main()