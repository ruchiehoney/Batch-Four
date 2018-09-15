print("This is my final Project on CODE LAGOS Training.")

print("ONAH MOSES")
print("Email:moszil2017@gmail.com")
print("Tel: 08069662468")
print("Instagram: onahzil")
print("Twitter: moszil20")

print("Training center:Lekki Phase 1 Center. \n Location:2 Babalola Garden (Wtech)")
print("Code Lagos Powered by Lagos state")

print("This work is  designed to used by anybody who needs to use exact amount of time frame.\n It can be used whn Reading,  studying, during Presentation, In an Event, Class Room Etc.")





print("This is Countdown timer.")





import tkinter as tk
import datetime as dt


class CountdownLabel(tk.Label):
    """ A Label in the format of HH:MM:SS, that displays counting down from given 
    seconds.
    """

    def __init__(self, master, seconds_left):
        super().__init__(master)
        self._seconds_left = seconds_left
        self._timer_on = False
        self._countdown()                   # Start counting down immediately

    def _start_countdown(self):
        self._stop_countdown()
        self._countdown()

    def _stop_countdown(self):
        if self._timer_on:
            self.after_cancel(self._timer_on)
            self._timer_on = False

    def _countdown(self):
        self['text'] = self._get_timedelta_from_seconds(self._seconds_left)
        if self._seconds_left:
            self._seconds_left -= 1
            self._timer_on = self.after(1000, self._countdown)

    @staticmethod
    def _get_timedelta_from_seconds(seconds):
        return dt.timedelta(seconds=seconds)


if __name__ == '__main__':
    root = tk.Tk()

    countdown = CountdownLabel(root, 50)

countdown.pack()
root.mainloop()
print("Your time is off")

