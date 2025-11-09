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


p =10
def scan_product(): 

    global p


    scanned_upc = upc_var.get()
    product_obj = Product.objects.filter(UPC=scanned_upc).first()

    if product_obj:
        # product_obj is now a single Product instance (or None if not found)
        prodPrice = product_obj.Price
        prodName = product_obj.Name
        print(f"Found Product: {prodName} | Price: {prodPrice}")
        receiptLineText = prodName + " $" + str(prodPrice) + " " + scanned_upc
        receiptLine_label = tk.Label(root, text=receiptLineText)

        receiptLine_label.grid(row=p, column=0, padx=5, pady=5)
        p = p +1

    else:
        # Handle the case where no product was found
        print(f"Error: No product found for UPC {scanned_upc}.")
        


        


def scan_product2(): 



    scanned_upc = upc_var.get()

    product_obj = Product.objects.filter(UPC=scanned_upc).first
    
    if product_obj:
        prodPrice = product_obj.Price
        prodName = product_obj.Name
        print(f"Found Product: {prodName} | Price: {prodPrice}")
    

        receiptLineText = prodName + " $" + prodPrice + " " + scanned_upc
        receiptLine_label = tk.Label(root, text=receiptLineText)

        receiptLine_label.grid(row=i, column=0, padx=5, pady=5)
        i = i +1



    
    
total = 0

root = tk.Tk()
root.title("Cash Register")
root.geometry("500x2000")

upc_var = tk.StringVar()

upc_label = tk.Label(root, text="Enter UPC")
upc_entry = tk.Entry(root, textvariable=upc_var)


scan_button = tk.Button(root, text="Scan/Submit", command=scan_product)

upc_label.grid(row=1, column=0, padx=5, pady=5)
upc_entry.grid(row=1, column=1, padx=5, pady=5)

scan_button.grid(row=2, column=0, columnspan=2, pady=10)



root.mainloop()
