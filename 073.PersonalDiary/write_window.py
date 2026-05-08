import tkinter as tk


class WriterApp(tk.Tk):
    def __init__(self, callback_f):
        super().__init__()

        self.callback_f = callback_f

        self.geometry("700x550")
        self.title("Write diary entry")
        self.resizable(False, False)

        self.build_ui()
        self.mainloop()

    def close_window(self):
        self.destroy()

    def save_text(self):
        self.callback_f(self.text_field.get("1.0", tk.END))
        self.destroy()

    def build_ui(self):
        self.rowconfigure(0, weight=8)
        self.rowconfigure(1, weight=1)

        self.text_field = tk.Text(self)
        self.text_field.grid(row=0, column=0)

        frame = tk.Frame(self, height=100)
        frame.grid(row=1, column=0, sticky="nsew")

        save_btn = tk.Button(frame, text="Save", command=self.save_text, pady=10)
        save_btn.pack(side="left", expand=True, fill="both")
        close_btn = tk.Button(frame, text="Close", command=self.close_window, pady=10)
        close_btn.pack(side="left", expand=True, fill="both")
