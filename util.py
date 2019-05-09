import sqlite3

def create_tables():
    con = sqlite3.connect("database.db")
    cursor = con.cursor()

    queries = [
        """CREATE TABLE IF NOT EXISTS Customer(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            password CHAR(14) NOT NULL, 
            email CHAR(320) NOT NULL UNIQUE, 
            name CHAR(50) NOT NULL, 
            surname CHAR(50) NOT NULL,
            city CHAR(14) NOT NULL)""",
        """CREATE TABLE IF NOT EXISTS CustomerAddress(
            customer_id CHAR(25) NOT NULL,
            phone_number CHAR(13) NOT NULL,
            city CHAR(14) NOT NULL,
            district CHAR(60) NOT NULL,
            address TEXT NOT NULL,
            address_description TEXT NOT NULL,
            FOREIGN KEY(customer_id) REFERENCES Customer(id))""",
    ]

    for query in queries:
        cursor.execute(query)
    
    con.commit()
    con.close()

def validate_register_form(register_form):
    pass

def validate_login():
    pass
