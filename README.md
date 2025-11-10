# Assignment 3 - SOFE 3650U

## Team Members
* **Zachary Matasic**
* **Mohamed Tawfik Omar**
* **Nithusan Kandasamy**

---

## Description
This project is a desktop cash register application built with Python. It uses **Tkinter** for the graphical user interface (GUI) and leverages the **Django ORM (Object-Relational Mapper)** as a standalone component to manage the product database.

---

## How to Run

1.  **Set up the database:**
    Before running the main application, you must create the database tables from the models.
    ```bash
    # Create the migration files (if not already done)
    python manage.py makemigrations db
    
    # Apply the migrations to create the database tables
    python manage.py migrate
    ```

2.  **Run the application:**
    Once the database is set up, you can run the Tkinter application.
    ```bash
    python main.py
    ```
    The application will launch a GUI window. The `main.py` script will also automatically seed the database with 19 sample products every time it starts.

---

## Code Overview & ORM Implementation

This repository demonstrates using the Django ORM outside of a typical Django web server. A review of the code clearly shows this separation.

* `main.py`:
    * This is the main executable for the project.
    * **GUI:** It builds the **Tkinter** interface (the cash register window, UPC entry, and scan button).
    * **Django Setup:** At the top of the file, it manually initializes the Django environment (`os.environ.setdefault`, `django.setup()`) to enable use of the ORM.
    * **ORM in Action (Create):** On launch, the script seeds the database using `Product.objects.create(...)` to add numerous sample products.
    * **ORM in Action (Query):** The `scan_product()` function is tied to the "Scan" button. It gets the text from the UPC entry and executes the query `Product.objects.filter(UPC=scanned_upc).first()` to find a matching product in the database.

* `db/models.py`:
    * This file is the core of the ORM. It defines the `Product` model, which inherits from `django.db.models.Model`.
    * The Django ORM uses this Python class to automatically create and manage the `Product` table in the database.

* `manage.py` & `settings.py`:
    * These are standard Django files. `settings.py` defines the database connection and lists `db` as an `INSTALLED_APP`. `manage.py` is the command-line utility used to run database migrations.

---

## File Structure
---------------------------------
django-orm/
├── db/
│   ├── __init__.py
│   └── models.py
├── main.py
├── manage.py
├── README.md
└── settings.py






