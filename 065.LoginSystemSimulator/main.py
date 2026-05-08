"""
Customtkinter sugar 😇🫠 :)
"""

import customtkinter as ctk
from tkinter import messagebox


USERNAME = "maverick"
PASSWORD = "helloworld123"


class LoginSystem(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Login System")
        self.geometry("400x500")
        self.resizable(False, False)

        self.username_var = ctk.StringVar()
        self.password_var = ctk.StringVar()

        self.build_ui()

        self.mainloop()

    def submit(self):
        username = self.username_var.get()
        password = self.password_var.get()

        if username == USERNAME and password == PASSWORD:
            print("Correct!")
            quit()
        else:
            messagebox.showerror("Error!", "Invalid credentials!")

    def build_ui(self):
        frame = ctk.CTkFrame(self, fg_color="#222222")
        frame.pack(expand=True, fill="both", padx=25)

        ctk.CTkLabel(frame, text="Login System", font=("Arial", 36, "bold"), justify="center").pack(expand=True, fill="x", pady=8)

        ctk.CTkLabel(frame, text="Username", justify="left", font=("Arial", 20)).pack(fill="x")
        username_field = ctk.CTkEntry(frame, textvariable=self.username_var, font=("Arial", 20))
        username_field.pack(fill="x", pady=5)

        ctk.CTkLabel(frame, text="Password", justify="left", font=("Arial", 20)).pack(fill="x")
        password_field = ctk.CTkEntry(frame, textvariable=self.password_var, font=("Arial", 20))
        password_field.pack(fill="x", pady=5)

        ctk.CTkButton(frame, text="Submit", command=self.submit, font=("Arial", 22)).pack(expand=True, fill="x")



if __name__ == '__main__':
    app = LoginSystem()
