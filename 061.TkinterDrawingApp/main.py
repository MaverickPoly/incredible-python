"""
Using ttk bootstraaaap hahaha)
"""
import ttkbootstrap as tk


class DrawingApp(tk.Window):
    def __init__(self):
        super().__init__()

        self.title("Drawing App")
        self.geometry("900x900")
        self.resizable(False, False)

        self.weight_var = tk.IntVar(value=1)
        self.color_var = tk.StringVar(value="black")

        self.create_widgets()

        self.start_pos = None

        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.end_drawing)

        self.bind("<Up>", lambda _: self.weight_var.set(min(self.weight_var.get() + 1, 20)))
        self.bind("<Down>", lambda _: self.weight_var.set(max(self.weight_var.get() - 1, 1)))

        self.mainloop()

    def clear_canvas(self):
        self.canvas.delete("all")

    def start_drawing(self, e):
        self.start_pos = (e.x, e.y)

    def end_drawing(self, e):
        self.start_pos = None

    def draw(self, e):
        if self.start_pos is not None:
            current_pos = (e.x, e.y)
            self.canvas.create_line(self.start_pos[0], self.start_pos[1], current_pos[0], current_pos[1],
                                    fill=self.color_var.get(), width=self.weight_var.get(), capstyle="round", smooth=True)
            self.start_pos = current_pos

    def create_widgets(self):
        # Controls frame
        controls_frame = tk.Frame(self)
        controls_frame.pack(fill="x")

        weight_label = tk.Label(controls_frame, textvariable=self.weight_var, font=("Arial", 20))
        weight_label.pack(fill="x", side="left")

        delete_btn = tk.Button(controls_frame, text="Clear", command=self.clear_canvas)
        delete_btn.pack(padx=5, side="left")

        colors_frame = tk.Frame(controls_frame)
        colors_frame.pack(side="right", fill="x", expand=True)

        colors = ["blue", "red", "black", "white", "yellow", "orange", "pink", "purple", "green", "gold", "cyan", "gray", "bisque", "brown"]

        for color in colors:
            color_frame = tk.Label(
                colors_frame,
                background=color,
                width=3,
                borderwidth=1
            )
            color_frame.bind("<Button-1>", lambda e, c=color: self.color_var.set(c))
            color_frame.pack(side="right", padx=2)


        # Canvas
        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.pack(expand=True, fill="both", side="top")


if __name__ == '__main__':
    app = DrawingApp()
