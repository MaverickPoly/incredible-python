import tkinter as tk
from datetime import datetime


class DigitalClock(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Digital Clock")
        self.geometry("300x300")
        self.resizable(False, False)

        self.create_widgets()

        self.mainloop()

    def update_time(self):
        now = datetime.now()
        self.label.configure(text=now.strftime("%H:%M:%S"))
        self.after(1000, self.update_time)

    def create_widgets(self):
        now = datetime.now()
        self.label = tk.Label(self, text=now.strftime("%H:%M:%S"), font=("Arial", 40))
        self.label.pack(expand=True, fill="both")

        self.after(1000, self.update_time)


if __name__ == '__main__':
    app = DigitalClock()
