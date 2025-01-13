import tkinter as tk
from tkinter import messagebox
class ATM:
    def __init__(self):
        self.accounts = {
            "12345": {"pin": "123", "balance": 100},
            "678911": {"pin": "324", "balance": 200}
        }
        self.selected_action = None

    def check_balance(self, pin, account_number):
        if account_number in self.accounts and self.accounts[account_number]["pin"] == pin:
            return f"Your balance is: ${self.accounts[account_number]['balance']}"
        else:
            return "Invalid account number or pin."

    def withdraw_money(self, pin, account_number, amount_to_withdraw):
        if account_number in self.accounts and self.accounts[account_number]["pin"] == pin:
            if self.accounts[account_number]["balance"] >= amount_to_withdraw:
                self.accounts[account_number]["balance"] -= amount_to_withdraw
                return f"Withdrawal successful! New balance: ${self.accounts[account_number]['balance']}"
            else:
                return "Insufficient balance."
        else:
            return "Invalid account number or pin."

    def deposit(self, pin, account_number, amount):
        if account_number in self.accounts and self.accounts[account_number]["pin"] == pin:
            self.accounts[account_number]["balance"] += amount
            return f"Deposit successful! New balance: ${self.accounts[account_number]['balance']}"
        else:
            return "Invalid account number or pin."

    def run(self):
        def show_auth_screen(action):
            self.selected_action = action
            main_menu.pack_forget()
            auth_screen.pack()

        def authenticate():
            account_number = entry_account.get()
            pin = entry_pin.get()
            if self.selected_action == "Check Balance":
                result = self.check_balance(pin, account_number)
                messagebox.showinfo("Check Balance", result)
                reset_to_main_menu()
            elif self.selected_action in ["Withdraw Money", "Deposit Money"]:
                auth_screen.pack_forget()
                transaction_screen.pack()

        def perform_transaction():
            account_number = entry_account.get()
            pin = entry_pin.get()
            try:
                amount = float(entry_amount.get())
                if self.selected_action == "Withdraw Money":
                    result = self.withdraw_money(pin, account_number, amount)
                elif self.selected_action == "Deposit Money":
                    result = self.deposit(pin, account_number, amount)
                messagebox.showinfo(self.selected_action, result)
                reset_to_main_menu()
            except ValueError:
                messagebox.showerror("Error", "Invalid amount entered.")

        def reset_to_main_menu():
            entry_account.delete(0, tk.END)
            entry_pin.delete(0, tk.END)
            entry_amount.delete(0, tk.END)
            transaction_screen.pack_forget()
            auth_screen.pack_forget()
            main_menu.pack()

        window = tk.Tk()
        window.geometry("400x300")
        window.title("ATM Simulator")

        # Main Menu
        main_menu = tk.Frame(window)
        tk.Label(main_menu, text="Welcome to the ATM", font=("Arial", 16)).pack(pady=10)
        tk.Button(main_menu, text="Check Balance", command=lambda: show_auth_screen("Check Balance")).pack(pady=5)
        tk.Button(main_menu, text="Withdraw Money", command=lambda: show_auth_screen("Withdraw Money")).pack(pady=5)
        tk.Button(main_menu, text="Deposit Money", command=lambda: show_auth_screen("Deposit Money")).pack(pady=5)
        main_menu.pack()

        # Authentication Screen
        auth_screen = tk.Frame(window)
        tk.Label(auth_screen, text="Enter Account Number and PIN", font=("Arial", 14)).pack(pady=10)
        tk.Label(auth_screen, text="Account Number:").pack(pady=5)
        entry_account = tk.Entry(auth_screen)
        entry_account.pack()
        tk.Label(auth_screen, text="PIN:").pack(pady=5)
        entry_pin = tk.Entry(auth_screen, show="*")
        entry_pin.pack()
        tk.Button(auth_screen, text="Submit", command=authenticate).pack(pady=10)
        tk.Button(auth_screen, text="Back", command=reset_to_main_menu).pack()

        # Transaction Screen
        transaction_screen = tk.Frame(window)
        tk.Label(transaction_screen, text="Enter Amount", font=("Arial", 14)).pack(pady=10)
        tk.Label(transaction_screen, text="Amount:").pack(pady=5)
        entry_amount = tk.Entry(transaction_screen)
        entry_amount.pack()
        tk.Button(transaction_screen, text="Submit", command=perform_transaction).pack(pady=10)
        tk.Button(transaction_screen, text="Back", command=reset_to_main_menu).pack()

        window.mainloop()


# Instantiate and run the ATM
atm = ATM()
atm.run()
