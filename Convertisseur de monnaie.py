import tkinter as tk
from forex_python.converter import CurrencyRates

conversions = []

def convert():
    cr = CurrencyRates()
    amount = int(amount_entry.get())
    from_currency = from_entry.get().upper()
    to_currency = to_entry.get().upper()
    output = cr.convert(from_currency, to_currency, amount)
    output_label.config(text="The converted rate is: " + str(output))
    conversions.append((amount, from_currency, to_currency, output))
    history_listbox.insert(tk.END, f"{amount} {from_currency} = {output} {to_currency}")

root = tk.Tk()
root.title("Convertisseur de monnaie")

amount_label = tk.Label(root, text="Enter amount:")
amount_label.grid(row=0, column=0)

amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1)

from_label = tk.Label(root, text="Convert from:")
from_label.grid(row=1, column=0)

from_entry = tk.Entry(root)
from_entry.grid(row=1, column=1)

to_label = tk.Label(root, text="Convert to:")
to_label.grid(row=2, column=0)

to_entry = tk.Entry(root)
to_entry.grid(row=2, column=1)

convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.grid(row=3, column=0, columnspan=2, pady=10)

output_label = tk.Label(root)
output_label.grid(row=4, column=0, columnspan=2)

history_label = tk.Label(root, text="History:")
history_label.grid(row=5, column=0, columnspan=2)

history_listbox = tk.Listbox(root)
history_listbox.grid(row=6, column=0, columnspan=2)

root.mainloop()

