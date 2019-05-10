import sqlite3
import re

def create_tables():
    con = sqlite3.connect("database.db")
    cursor = con.cursor()

    queries = [
        """CREATE TABLE IF NOT EXISTS Customer(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            password CHAR(14) NOT NULL, 
            email CHAR(320) NOT NULL UNIQUE, 
            name VARCHAR(100) NOT NULL, 
            surname VARCHAR(100) NOT NULL,
            city CHAR(14) NOT NULL)""",
        """CREATE TABLE IF NOT EXISTS CustomerAddress(
            customer_id INTEGER NOT NULL,
            phone_number CHAR(13) NOT NULL,
            city CHAR(14) NOT NULL,
            district VARCHAR(255) NOT NULL,
            address TEXT NOT NULL,
            address_description TEXT NOT NULL,
            FOREIGN KEY(customer_id) REFERENCES Customer(id))""",
    ]

    for query in queries:
        cursor.execute(query)
    
    con.commit()
    con.close()

def validate_register_form(register_form):
    #VALIDATING E-MAIL
    if not email_is_valid(register_form['email']):
        print("invalid e-mail")
    #VALIDATING NAME
    if not register_form['name'].replace(" ","").isalpha():
        print("invalid name")
    #VALIDATING SURNAME
    if not register_form['surname'].replace(" ", "").isalpha():
        print("invalid surname")
    #VALIDATING PASSWORD
    #VALIDATING PASSWORD CONFIRMATION

def validate_login():
    pass


def email_is_valid(email):
    if len(email) > 320 or not re.match(r"[^@]+@[^@]+\.[^@]+", email) or '' in email:
        return False
    return True
