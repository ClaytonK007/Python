from tkinter import *

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
    text_ounce.insert(END, f"{ounce:.2f} ounce")

def clear_results():
    entry_kg.delete(0, END)
    text_gram.delete("1.0", END)
    text_pound.delete("1.0", END)
    text_ounce.delete("1.0", END)

#   Create the main GUI window
window = Tk()
window.title("Weight Converter")

#   Create labels and widgets
label_kg = Label(window, text="Input the weight in KG")
entry_kg = Entry(window)
label_gram = Label(window, text="Gram")
text_gram = Text(window, height=1, width=30)
label_pound = Label(window, text="Pound")
text_pound = Text(window, height=1, width=30)
label_ounce = Label(window, text="Ounce")
text_ounce = Text(window, height=1, width=30)
button_convert = Button(window, text="Convert", command=convert_weight)
button_clear = Button(window, text="Clear", command=clear_results)

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

#   Run GUI
window.mainloop()