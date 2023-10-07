from forex_python.converter import CurrencyRates
import tkinter as tk

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")

        self.currency_converter = CurrencyRates()

        self.from_currency_var = tk.StringVar()
        self.from_currency_var.set("USD")
        self.to_currency_var = tk.StringVar()
        self.to_currency_var.set("EUR")
        self.amount_var = tk.StringVar()
        self.result_var = tk.StringVar()

        self.from_currency_label = tk.Label(root, text="From Currency:")
        self.from_currency_label.pack()
        self.from_currency_entry = tk.Entry(root, textvariable=self.from_currency_var)
        self.from_currency_entry.pack()

        self.to_currency_label = tk.Label(root, text="To Currency:")
        self.to_currency_label.pack()
        self.to_currency_entry = tk.Entry(root, textvariable=self.to_currency_var)
        self.to_currency_entry.pack()

        self.amount_label = tk.Label(root, text="Amount:")
        self.amount_label.pack()
        self.amount_entry = tk.Entry(root, textvariable=self.amount_var)
        self.amount_entry.pack()

        self.convert_button = tk.Button(root, text="Convert", command=self.convert_currency)
        self.convert_button.pack()

        self.result_label = tk.Label(root, textvariable=self.result_var, font=("Arial", 18))
        self.result_label.pack()

    def convert_currency(self):
        from_currency = self.from_currency_var.get()
        to_currency = self.to_currency_var.get()
        amount = float(self.amount_var.get())
        converted_amount = self.currency_converter.convert(from_currency, to_currency, amount)
        self.result_var.set(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

if __name__ == "__main__":
    root = tk.Tk()
    converter = CurrencyConverter(root)
    root.mainloop()
