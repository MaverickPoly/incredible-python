import tkinter as tk


class TemperatureConverter(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Temperature Converter")
        self.geometry("500x500")
        self.resizable(False, False)

        self.celsius_var = tk.DoubleVar(value=0.0)
        self.fahrenheit_var = tk.DoubleVar(value=0.0)

        self.build_ui()

        self.mainloop()

    def to_fahrenheit(self):
        celsius_value = self.celsius_var.get()
        fahr_val = (celsius_value * 9 / 5) + 32
        self.fahrenheit_var.set(round(fahr_val, 1))

    def to_celsius(self):
        fahr_val = self.fahrenheit_var.get()
        celsius_val = (fahr_val - 32) * 5 / 9
        self.celsius_var.set(round(celsius_val, 1))

    def build_ui(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        frame1 = tk.Frame(self)
        tk.Label(frame1, text="Celsius").pack(expand=True, fill="both")
        tk.Entry(frame1, textvariable=self.celsius_var).pack(fill="both")
        tk.Button(frame1, text="Convert", command=self.to_fahrenheit).pack(expand=True, fill="x")
        frame1.grid(column=0, row=0, sticky="nsew", padx=10, pady=20)

        frame2 = tk.Frame(self)
        tk.Label(frame2, text="Fahrenheit").pack(expand=True, fill="both")
        tk.Entry(frame2, textvariable=self.fahrenheit_var).pack(fill="both")
        tk.Button(frame2, text="Convert", command=self.to_celsius).pack(expand=True, fill="x")
        frame2.grid(column=1, row=0, sticky="nsew", padx=10, pady=20)


if __name__ == '__main__':
    app = TemperatureConverter()
