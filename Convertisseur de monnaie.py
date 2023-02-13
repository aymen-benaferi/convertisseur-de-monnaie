import tkinter as tk

def convert():
    conversion_rates = {
        'USD': {'EUR': 0.82, 'JPY': 109.77, 'MXN': 21.42},
        'EUR': {'USD': 1.22, 'JPY': 132.51, 'MXN': 26.11},
        'JPY': {'USD': 0.0091, 'EUR': 0.0075, 'MXN': 0.19},
        'MXN': {'USD': 0.047, 'EUR': 0.038, 'JPY': 5.26}
    }

    amount = int(amount_entry.get())
    from_currency = from_entry.get().upper()
    to_currency = to_entry.get().upper()
    output = amount * conversion_rates[from_currency][to_currency]
    output_label.config(text="The converted rate is: " + str(output))
    conversions.append((amount, from_currency, to_currency, output))
    history_listbox.insert(
        tk.END, f"{amount} {from_currency} = {output} {to_currency}")


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

history_label = tk.Label(root, text="Historique:")
history_label.grid(row=5, column=0, columnspan=2)

history_listbox = tk.Listbox(root)
history_listbox.grid(row=6, column=0, columnspan=2)

root.mainloop()


