import requests
import tkinter as tk
from tkinter import ttk, messagebox

#   Configure API
API_KEY = "YOUR_API"
URL =  f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

#   Functions to fetch exchange rates from API
def get_exchange_rate(from_currency, to_currency):
    try:
        response = requests.get(f"{URL}{from_currency}")
        data = response.json()
        if data["result"] == "success":
            return data["conversion_rates"][to_currency]
        else:
            return None
    except Exception as e:
        messagebox.showerror(f"Error: {e}")
        return None

#   Get inputs, calculate and display on GUI
def perform_conversion():
    amount = float(amount_entry.get())
    from_curr = from_currency_combo.get()
    to_curr = to_currency_combo.get()

    rate = get_exchange_rate(from_curr, to_curr)
    if rate:
        result = amount * rate
        result_label.config(text=f"{amount} {from_curr} = {result:.2f} {to_curr}")
    else:
        messagebox.showerror("Error,","Could not fetch rate.")

#   GUI setup
root = tk.Tk()
root.title("Currency Converter")
root.geometry("300x250")

#   Widgets
tk.Label(root, text="Amount:").pack(pady=5)
amount_entry = tk.Entry(root)
amount_entry.pack()

#   Dropdowns for currencies
currencies = ["USD", "EUR", "GBP", "INR", "JPY", "ZAR"]
from_currency_combo = ttk.Combobox(root, value=currencies)
from_currency_combo.current(0)
from_currency_combo.pack(pady=5)

to_currency_combo = ttk.Combobox(root, value=currencies)
to_currency_combo.current(1)
to_currency_combo.pack(pady=5)

#   Convert button and result label
convert_button = tk.Button(root, text="Convert", command=perform_conversion)
convert_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Helvetica", 12, "bold"))
result_label.pack(pady=10)

#   Start application
root.mainloop()

