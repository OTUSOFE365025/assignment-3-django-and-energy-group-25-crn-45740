############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys

sys.dont_write_bytecode = True

# Import settings
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# setup django environment
import django

django.setup()

# Import your models for use in your script
from db.models import *

import tkinter as tk

############################################################################
## START OF APPLICATION
############################################################################
""" Replace the code below with your own """

# Seed a few Products in the database
Product.objects.create(UPC='12345', Name='Coffee', Price=8.32)
Product.objects.create(UPC='67890', Name='Muffin', Price=2.50)
Product.objects.create(UPC='11111', Name='Tea', Price=3.99)
Product.objects.create(UPC='22222', Name='Sandwich', Price=6.75)
Product.objects.create(UPC='33333', Name='Bagel', Price=2.99)
Product.objects.create(UPC='44444', Name='Croissant', Price=4.25)
Product.objects.create(UPC='55555', Name='Juice', Price=5.50)
Product.objects.create(UPC='66666', Name='Donut', Price=1.99)
Product.objects.create(UPC='77777', Name='Cookie', Price=2.25)
Product.objects.create(UPC='88888', Name='Water', Price=1.50)
Product.objects.create(UPC='99999', Name='Cabbage', Price=2.50)
Product.objects.create(UPC='12222', Name='Tea', Price=1.50)
Product.objects.create(UPC='12333', Name='Milk', Price=5.00)
Product.objects.create(UPC='12344', Name='Carrot', Price=2.25)
Product.objects.create(UPC='13333', Name='Lettuce', Price=4.15)
Product.objects.create(UPC='13244', Name='Apple', Price=1.50)
Product.objects.create(UPC='14223', Name='Egg', Price=1.25)
Product.objects.create(UPC='20833', Name='Chips', Price=3.00)
Product.objects.create(UPC='21334', Name='Cheese', Price=3.25)

for u in Product.objects.all():
    print(f'ID: {u.id} \tProductname: {u.Name}')

    i = 3

total = 0.00
rowHeight = 4


def scan_product():
    global rowHeight
    global total

    scanned_upc = upc_var.get()
    product_obj = Product.objects.filter(UPC=scanned_upc).first()

    if product_obj:
        prodPrice = product_obj.Price
        prodName = product_obj.Name
        total = total + prodPrice
        # print(f"Found Product: {prodName} | Price: {prodPrice}")
        receiptLineProduct_label = tk.Label(root, text=prodName)
        receiptLinePrice_label = tk.Label(root, text=str(prodPrice))
        receiptLineUPC_label = tk.Label(root, text=scanned_upc)

        receiptLineProduct_label.grid(row=rowHeight, column=0, padx=5, pady=5, sticky="w")
        receiptLinePrice_label.grid(row=rowHeight, column=2, padx=5, pady=5, sticky="w")
        receiptLineUPC_label.grid(row=rowHeight, column=1, padx=5, pady=5, sticky="w")

        totalLine_label.config(text="$" + str(total))

        totalText_Label.grid_forget()
        totalLine_label.grid_forget()

        totalText_Label.grid(row=rowHeight + 1, column=0, padx=5, pady=5, sticky="w")
        totalLine_label.grid(row=rowHeight + 1, column=2, padx=5, pady=5, sticky="w")

        rowHeight = rowHeight + 1



    else:
        print(f"Error: No product found for UPC {scanned_upc}.")


root = tk.Tk()
root.title("Cash Register")
root.geometry("600x800")

upc_var = tk.StringVar()

upc_label = tk.Label(root, text="Enter UPC")
upc_entry = tk.Entry(root, textvariable=upc_var)
scan_button = tk.Button(root, text="Scan", command=scan_product)
receiptHeaderProduct_label = tk.Label(root, text="Product")
receiptHeaderPrice_label = tk.Label(root, text="Price")
receiptHeaderUPC_label = tk.Label(root, text="UPC")

upc_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
upc_entry.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
scan_button.grid(row=2, column=2, pady=10, sticky="e")

receiptHeaderProduct_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
receiptHeaderPrice_label.grid(row=3, column=2, padx=5, pady=5, sticky="w")
receiptHeaderUPC_label.grid(row=3, column=1, padx=5, pady=5, sticky="w")

totalText_Label = tk.Label(root, text="Total is")
totalLine_label = tk.Label(root, text="$" + str(total))

root.mainloop()


