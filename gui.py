# gui.py

import tkinter as tk
from tkinter import messagebox, Toplevel, Label
from customer import Customer
from order import Order
from menu_items import MakeupItem, Lipstick, Foundation
from database import save_order_to_db

def show_invoice(order):
    invoice_win = Toplevel()
    invoice_win.title("🧾 Invoice")
    invoice_win.geometry("300x350")
    invoice_win.config(bg="#fdf6f9")

    Label(invoice_win, text=f"Invoice for {order.customer.name}", font=("Segoe UI", 12, "bold"), bg="#fdf6f9").pack(pady=10)

    for item in order.items:
        Label(invoice_win, text=f"{item.name} - ${item.price}", font=("Segoe UI", 11), bg="#fdf6f9").pack()

    Label(invoice_win, text=f"------------------------", bg="#fdf6f9").pack()
    Label(invoice_win, text=f"Total: ${order.total_price()}", font=("Segoe UI", 12, "bold"), fg="#c2185b", bg="#fdf6f9").pack(pady=10)

def place_order():
    customer_name = name_entry.get().strip()
    if not customer_name:
        messagebox.showerror("Error", "Please enter a name")
        return

    customer = Customer(customer_name)
    order = Order(customer)

    if lipstick_var.get():
        order.add_item(Lipstick("Red Lipstick", 45))
    if gloss_var.get():
        order.add_item(Lipstick("Lip Gloss", 35))
    if foundation_var.get():
        order.add_item(Foundation("Liquid Foundation", 80))
    if compact_var.get():
        order.add_item(Foundation("Compact Powder", 60))

    if not order.items:
        messagebox.showwarning("No Items", "Select at least one item.")
        return

    save_order_to_db(customer, order.items)
    show_invoice(order)

# GUI setup
root = tk.Tk()
root.title("💄 Makeup Store Order System")
root.geometry("320x470")
root.config(bg="#fff0f5")

tk.Label(root, text="Customer Name:", font=("Segoe UI", 12, "bold"), bg="#fff0f5").pack(pady=(10, 0))
name_entry = tk.Entry(root, font=("Segoe UI", 12))
name_entry.pack(pady=5)

tk.Label(root, text="Select Lip Products:", font=("Segoe UI", 12, "bold"), bg="#fff0f5", fg="#c2185b").pack(pady=(10, 0))
lipstick_var = tk.IntVar()
gloss_var = tk.IntVar()
tk.Checkbutton(root, text="💋 Red Lipstick", variable=lipstick_var, bg="#fff0f5").pack()
tk.Checkbutton(root, text="✨ Lip Gloss", variable=gloss_var, bg="#fff0f5").pack()

tk.Label(root, text="Select Face Products:", font=("Segoe UI", 12, "bold"), bg="#fff0f5", fg="#7b1fa2").pack(pady=(10, 0))
foundation_var = tk.IntVar()
compact_var = tk.IntVar()
tk.Checkbutton(root, text="🧴 Liquid Foundation", variable=foundation_var, bg="#fff0f5").pack()
tk.Checkbutton(root, text="🌸 Compact Powder", variable=compact_var, bg="#fff0f5").pack()

tk.Button(root, text="Place Order", font=("Segoe UI", 12, "bold"), bg="#ec407a", fg="white", command=place_order).pack(pady=20)

root.mainloop()
