import tkinter as tk
from tkinter import *
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Weight Converter")
        self.geometry("850x150")

        # Dictionary to store frames
        self.frames = {}
        
        # Initialize Frames
        for F in (ScreenOne, ScreenTwo, ScreenThree):
            frame = F(self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show the first screen
        self.show_frame(ScreenOne)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class ScreenOne(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        label = tk.Label(self, text="Select an Option")
        label.pack(pady=10)

        # Dropdown Option
        self.option = tk.StringVar(self)
        dropdown = ttk.Combobox(self, values=["Convert Kgs", "Convert Pounds"], state="readonly")
        dropdown.set("Convert Kgs")
        dropdown.pack(pady=10)

        # "Next" button
        btn = tk.Button(self, text="Next", 
                        command=lambda: self.check_option(parent))
        btn.pack(pady=10)

    def check_option(self, parent):
        # IF condition to check choice
        if self.option.get() == "Convert Kgs":
            parent.show_frame(ScreenTwo)
        else:
            parent.show_frame(ScreenThree)

class ScreenTwo(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        grid_frame = tk.Frame(self)
        grid_frame.pack()

        def convert_weight():
            #   Retrieve input value from entry widget
            kg_value = float(entry_kg.get())

            #   Perform conversions
            gram = kg_value * 1000
            pound = kg_value * 2.20462
            ounce = kg_value * 35.274

            #   Return the results to widgets
            text_gram.delete("1.0", END)
            text_gram.insert(END, f"{gram:.2f} grams")
            text_pound.delete("1.0", END)
            text_pound.insert(END, f"{pound:.2f} pounds")
            text_ounce.delete("1.0", END)
            text_ounce.insert(END, f"{ounce:.2f} ounces")

        def clear_results():
            entry_kg.delete(0, END)
            text_gram.delete("1.0", END)
            text_pound.delete("1.0", END)
            text_ounce.delete("1.0", END)
        
        #   Create labels and widgets
        label_kg = tk.Label(grid_frame, text="Input the weight in KG")
        entry_kg = tk.Entry(grid_frame)
        label_gram = tk.Label(grid_frame, text="Gram")
        text_gram = tk.Text(grid_frame, height=1, width=30)
        label_pound = tk.Label(grid_frame, text="Pound")
        text_pound = tk.Text(grid_frame, height=1, width=30)
        label_ounce = tk.Label(grid_frame, text="Ounces")
        text_ounce = tk.Text(grid_frame, height=1, width=30)
        button_convert = tk.Button(grid_frame, text="Convert", command=convert_weight)
        button_clear = tk.Button(grid_frame, text="Clear", command=clear_results)
        button_back = tk.Button(grid_frame, text="Back", command=lambda: parent.show_frame(ScreenOne))

        #   Create grid for labels and widgets
        label_kg.grid(row=0, column=0, padx=10, pady=10)
        entry_kg.grid(row=0, column=1, padx=10, pady=10)
        label_gram.grid(row=1, column=0)
        label_pound.grid(row=1, column=1)
        label_ounce.grid(row=1, column=2)
        text_gram.grid(row=2, column=0, padx=10, pady=10)
        text_pound.grid(row=2, column=1, padx=10, pady=10)
        text_ounce.grid(row=2, column=2, padx=10, pady=10)
        button_convert.grid(row=0, column=2, padx=10, pady=10)
        button_clear.grid(row=2, column=3, padx=10, pady=10)
        button_back.grid(row=3, column=1)

class ScreenThree(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        grid_frame = tk.Frame(self)
        grid_frame.pack()

        def convert_weight():
            #   Retrieve input value from entry widget
            pound_value = float(entry_pound.get())

            #   Perform conversions
            gram = pound_value * 453.59237
            kg = pound_value / 2.20462
            ounce = pound_value * 16

            #   Return the results to widgets
            text_gram.delete("1.0", END)
            text_gram.insert(END, f"{gram:.2f} grams")
            text_kg.delete("1.0", END)
            text_kg.insert(END, f"{kg:.2f} pounds")
            text_ounce.delete("1.0", END)
            text_ounce.insert(END, f"{ounce:.2f} ounces")

        def clear_results():
            entry_pound.delete(0, END)
            text_gram.delete("1.0", END)
            text_kg.delete("1.0", END)
            text_ounce.delete("1.0", END)
        
        #   Create labels and widgets
        label_pound = tk.Label(grid_frame, text="Input the weight in Pounds")
        entry_pound = tk.Entry(grid_frame)
        label_gram = tk.Label(grid_frame, text="Gram")
        text_gram = tk.Text(grid_frame, height=1, width=30)
        label_kg = tk.Label(grid_frame, text="Kg")
        text_kg = tk.Text(grid_frame, height=1, width=30)
        label_ounce = tk.Label(grid_frame, text="Ounces")
        text_ounce = tk.Text(grid_frame, height=1, width=30)
        button_convert = tk.Button(grid_frame, text="Convert", command=convert_weight)
        button_clear = tk.Button(grid_frame, text="Clear", command=clear_results)
        button_back = tk.Button(grid_frame, text="Back", command=lambda: parent.show_frame(ScreenOne))

        #   Create grid for labels and widgets
        label_pound.grid(row=0, column=0, padx=10, pady=10)
        entry_pound.grid(row=0, column=1, padx=10, pady=10)
        label_gram.grid(row=1, column=0)
        label_kg.grid(row=1, column=1)
        label_ounce.grid(row=1, column=2)
        text_gram.grid(row=2, column=0, padx=10, pady=10)
        text_kg.grid(row=2, column=1, padx=10, pady=10)
        text_ounce.grid(row=2, column=2, padx=10, pady=10)
        button_convert.grid(row=0, column=2, padx=10, pady=10)
        button_clear.grid(row=2, column=3, padx=10, pady=10)
        button_back.grid(row=3, column=1)

if __name__ == "__main__":
    app = App()
    app.mainloop()