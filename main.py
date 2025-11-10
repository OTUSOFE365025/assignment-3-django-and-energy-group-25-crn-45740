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
rowHeight =4

def scan_product(): 

    global rowHeight
    global total


    scanned_upc = upc_var.get()
    product_obj = Product.objects.filter(UPC=scanned_upc).first()

    if product_obj:
        prodPrice = product_obj.Price
        prodName = product_obj.Name
        total = total + prodPrice
        #print(f"Found Product: {prodName} | Price: {prodPrice}")
        receiptLineText = prodName + "\t\t\t$" + str(prodPrice) + "\t\t\t" + scanned_upc
        receiptLine_label = tk.Label(root, text=receiptLineText)

        receiptLine_label.grid(row=rowHeight, column=0, padx=5, pady=5)
        

        totalText = "TOTAL:\t\t\t\t\t\t$" + str(total)
        totalLine_label = tk.Label(root, text=totalText)
        totalLine_label.grid(row=rowHeight+ 1, column=0, padx=5, pady=5)

        rowHeight = rowHeight +1

        

    else:
        print(f"Error: No product found for UPC {scanned_upc}.")

root = tk.Tk()
root.title("Cash Register")
root.geometry("500x800")

upc_var = tk.StringVar()

root.grid_columnconfigure(2, weight=1)

upc_label = tk.Label(root, text="Enter UPC")
upc_entry = tk.Entry(root, textvariable=upc_var)
scan_button = tk.Button(root, text="Scan", command=scan_product)
receiptHeader_label = tk.Label(root, text="Product\t\t\tPrice\t\t\tUPC")


upc_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
upc_entry.grid(row=2, column=0, padx=5, pady=5, sticky="w")
scan_button.grid(row=2, column=2, columnspan=2, pady=10, sticky="e")
receiptHeader_label.grid(row=3, column=0, columnspan=5, padx=5, pady=5, sticky="w")

root.mainloop()



