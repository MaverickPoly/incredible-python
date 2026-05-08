import tkinter as tk
from tkinter import filedialog


class Notepad(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("600x600")
        self.title("Notepad clone")
        self.resizable(False, False)

        self.current_file = None

        self.create_ui()

        self.mainloop()

    def save_file(self):
        if not self.current_file:
            file = filedialog.asksaveasfilename()
            if not file: return
            self.current_file = file

        text_content = self.text_area.get("1.0", tk.END)
        with open(self.current_file, "w") as f:
            f.write(text_content)


    def open_file(self):
        file = filedialog.askopenfilename()
        if not file: return
        self.current_file = file

        with open(self.current_file, "r") as f:
            text_content = f.read()
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert("1.0", text_content)

    def new_file(self):
        current_content = self.text_area.get("1.0", tk.END)
        if current_content:
            self.save_file()

        self.current_file = None
        self.text_area.delete("1.0", tk.END)

    def about_screen(self):
        new_window = tk.Toplevel()
        new_window.geometry("300x300")
        new_window.resizable(False, False)

        label = tk.Label(new_window, text="This is a simple notepad clone auth implemented in Tkinter Python!", wraplength=300)
        label.pack(expand=True, fill="both")

    def create_ui(self):
        # Menu
        menu = tk.Menu(self)

        file_menu = tk.Menu(menu, tearoff=0)
        file_menu.add_command(
            label="Save",
            command=self.save_file
        )
        file_menu.add_command(
            label="Open",
            command=self.open_file
        )
        file_menu.add_command(
            label="New",
            command=self.new_file
        )
        menu.add_cascade(label="File", menu=file_menu)

        help_menu = tk.Menu(menu, tearoff=0)
        help_menu.add_command(
            label="About",
            command=self.about_screen
        )
        help_menu.add_command(
            label="Quit",
            command=quit
        )
        menu.add_cascade(label="Help", menu=help_menu)


        self.config(menu=menu)

        # Current file label

        # Body
        self.text_area = tk.Text(self)
        self.text_area.pack(expand=True, fill="both")


if __name__ == '__main__':
    app = Notepad()
