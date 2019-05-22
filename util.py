import sqlite3
import re

def create_tables():
    con = sqlite3.connect("database.db")
    cursor = con.cursor()

    queries = [
        """CREATE TABLE IF NOT EXISTS Customer(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email CHAR(320) NOT NULL UNIQUE, 
            password CHAR(14) NOT NULL, 
            name CHAR(100) NOT NULL, 
            surname CHAR(100) NOT NULL)""",
        """CREATE TABLE IF NOT EXISTS CustomerAddress(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            phone_number CHAR(11) NOT NULL,
            city CHAR(14) NOT NULL,
            town CHAR(50) NOT NULL,
            district CHAR(255) NOT NULL,
            address CHAR(300) NOT NULL,
            address_description CHAR(300) NOT NULL,
            FOREIGN KEY(customer_id) REFERENCES Customer(id))""",
        """CREATE TABLE IF NOT EXISTS Restaurant(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name CHAR(200) NOT NULL UNIQUE,
            city CHAR(14) NOT NULL,
            town CHAR(50) NOT NULL,
            district CHAR(20) NOT NULL,
            address CHAR(400) NOT NULL,
            phone_number CHAR(11) NOT NULL UNIQUE,
            owner_ssn INTEGER NOT NULL,
            owner_name CHAR(100) NOT NULL,
            owner_surname CHAR(100) NOT NULL,
            owner_phone_number CHAR(11) NOT NULL,
            email CHAR(320) NOT NULL UNIQUE,
            password CHAR(14) NOT NULL)""",
        """CREATE TABLE IF NOT EXISTS Product(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name CHAR(200) NOT NULL,
            price REAL NOT NULL,
            description CHAR(200),
            restaurant_id INTEGER NOT NULL,
            FOREIGN KEY(restaurant_id) REFERENCES Restaurant(id))""",
        """CREATE TABLE IF NOT EXISTS Order_(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            address_id INTEGER NOT NULL,
            total_price REAL NOT NULL,
            date TEXT NOT NULL,
            state CHAR(13) DEFAULT 'Onay Bekliyor',
            FOREIGN KEY(address_id) REFERENCES CustomerAddress(id))""",
        """CREATE TABLE IF NOT EXISTS SoldProduct(
            order_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            product_amount INTEGER NOT NULL,
            price REAL NOT NULL,
            FOREIGN KEY(order_id) REFERENCES Order_(id),
            FOREIGN KEY(product_id) REFERENCES Product(id))""",
    ]

    for query in queries:
        cursor.execute(query)
    
    con.commit()
    con.close()


def create_order(address_id, total_price, date):
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    cursor.execute('INSERT INTO Order_ (address_id, total_price, date) VALUES (?,?,?)',
                   (address_id, total_price, date))
    order_id = cursor.lastrowid
    con.commit()
    con.close()
    return order_id


def create_sold_product(order_id, product_id, product_amount, price):
    con = sqlite3.connect('database.db')
    cursor = con.cursor()
    cursor.execute('INSERT INTO SoldProduct (order_id, product_id, product_amount, price) VALUES (?,?,?,?)',
                   (order_id, product_id, product_amount, price))
    con.commit()
    con.close()

def validate_user_register(register_form):
    #VALIDATING E-MAIL
    if not email_is_valid(register_form['email']):
        return {'validated':False, 'message':'Hatalı E-Posta Girdiniz.'}
    #VALIDATING NAME
    if not register_form['name'].replace(" ","").isalpha():
        return {'validated':False, 'message':'Adı Kontrol Ediniz.'}
    #VALIDATING SURNAME
    if not register_form['surname'].replace(" ", "").isalpha():
        return {'validated':False, 'message':'Soyadı Kontrol Ediniz.'}
    #VALIDATING PASSWORD
    if len(register_form['password']) < 8:
        return {'validated':False, 'message':'Şifre 8-14 Karakter Olmalıdır.'}
    #VALIDATING PASSWORD CONFIRMATION
    if register_form['password'] != register_form['password_confirmation']:
        return {'validated':False, 'message':'Şifreler Uyuşmuyor.'}

    return {'validated':True, 'message':'Başarıyla Kayıt Oldunuz!'}


def validate_owner_register(register_form):
    #VALIDATING RESTAURANT NAME
    if len(register_form["name"]) == 0:
        return {'validated':False, 'message':'Restoran Adını Kontrol Ediniz.'}
    #VALIDATING SSN
    if len(register_form["owner_ssn"]) != 11:
        return {'validated':False, 'message':"TCKN'yi Kontrol Ediniz."}
    if len(register_form["address"]) == 0:
        return {'validated':False, 'message':"Adresi Kontrol Ediniz."}
    #VALIDATING OWNER NAME
    if not register_form["owner_name"].replace(" ", "").isalpha():
        return {'validated': False, 'message': 'Adı Kontrol Ediniz.'}
    #VALIDATING OWNER SURNAME
    if not register_form['owner_surname'].replace(" ", "").isalpha():
        return {'validated': False, 'message': 'Soyadı Kontrol Ediniz.'}
    #VALIDATING OWNER PHONE NO
    if len(register_form["owner_phone_number"]) != 11 or not register_form["owner_phone_number"].startswith("0") or ',' in register_form["owner_phone_number"]:
        return {'validated': False, 'message': 'Telefon Numarası 0xxxxxxxxxxxx Olmalıdır.'}
    #VALIDATING RESTAURANT PHONE NO
    if len(register_form["phone_number"]) != 11 or not register_form["phone_number"].startswith("0") or ',' in register_form["phone_number"]:
        return {'validated': False, 'message': 'Restoran Telefonu 0xxxxxxxxxx Olmalıdır.'}
    #VALIDATING E-MAIL
    if not email_is_valid(register_form["email"]):
        return {'validated': False, 'message': 'Hatalı E-Posta Girdiniz.'}
    #VALIDATING PASSWORD
    if len(register_form['password']) < 8:
        return {'validated': False, 'message': 'Şifre 8-14 Karakter Olmalıdır.'}
    #VALIDATING PASSWORD CONFIRMATION
    if register_form['password'] != register_form['password_confirmation']:
        return {'validated': False, 'message': 'Şifreler Uyuşmuyor.'}
    
    return {'validated': True, 'message': 'Başarıyla Kayıt Oldunuz!'}


def validate_address(address_form):
    if len(address_form["phone_number"]) != 11 or not address_form["phone_number"].startswith("0") or ',' in address_form["phone_number"]:
        return {'validated': False, 'message': 'Telefon Numarası 0xxxxxxxxxxxx Olmalıdır.'}
    if len(address_form['address']) == 0 or len(address_form['address_description']) == 0:
        return {'validated': False, 'message': 'Bütün Alanlar Zorunludur'}
    
    return {'validated': True, 'message': 'Adres Kaydedildi!'}

def email_is_valid(email):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email) or ' ' in email:
        return False
    return True


def save_customer(register_form):
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    form_tuple = (register_form['email'], register_form['password'], register_form['name'], register_form['surname'])
    cursor.execute('INSERT INTO Customer (email,password,name,surname) values (?,?,?,?)', form_tuple)
    con.commit()
    con.close()

def save_restaurant(register_form):
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    form_tuple = (register_form['name'], register_form['city'], register_form['town'],
                  register_form['district'], register_form['address'], register_form['phone_number'],
                  register_form['owner_ssn'], register_form['owner_name'], register_form['owner_surname'],
                  register_form['owner_phone_number'], register_form['email'], register_form['password'])

    cursor.execute('''INSERT INTO Restaurant (name, city, town, district, address, phone_number, owner_ssn, owner_name, 
                      owner_surname, owner_phone_number, email, password) values (?,?,?,?,?,?,?,?,?,?,?,?)''', form_tuple)
    con.commit()
    con.close()


def save_product(name, description, price, restaurant_id):
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    cursor.execute('INSERT INTO Product (name, price, description, restaurant_id) values (?,?,?,?)',
                   (name, price, description, restaurant_id))

    con.commit()
    con.close()


def save_address(address_form):
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    query = """INSERT INTO CustomerAddress 
    (phone_number, city, town, district, address, address_description, customer_id) 
    VALUES (?,?,?,?,?,?,?)"""

    cursor.execute(query,
                   (address_form['phone_number'], address_form['city'], address_form['town'], address_form['district'],
                    address_form['address'], address_form['address_description'], address_form['user_id']))

    con.commit()
    con.close()

def authenticate_user(login_form):
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    cursor.execute('SELECT id FROM Customer WHERE email=? AND password=?', (login_form['email'], login_form['password']))
    user = cursor.fetchone()
    try:
        if len(user) != 0:
            return user[0]
    except:
        return -1


def authenticate_owner(login_form):
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    cursor.execute('SELECT id FROM Restaurant WHERE email=? AND password=?', (login_form['email'], login_form['password']))
    user = cursor.fetchone()
    try:
        if len(user) != 0:
            return user[0]
    except:
        return -1


def update_product(name, description, price, product_id):
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    cursor.execute('UPDATE Product SET name = ?, description = ?, price = ? WHERE id = ?', (name, description, price, product_id))
    con.commit()
    con.close()


def update_order_state(product_id, new_state):
    con = sqlite3.connect('database.db')
    cursor = con.cursor()
    cursor.execute('UPDATE Order_ SET state = ? WHERE id = ?',
                   (new_state, product_id))
    con.commit()
    con.close()

def find_restaurants(city, town, district):
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    cursor.execute('SELECT id, name FROM Restaurant WHERE city = ? AND town = ? AND district = ?', (city, town, district))
    result = cursor.fetchall()
    con.close()
    return result

def find_products(restaurant_id):
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    cursor.execute('SELECT id, name, price, description FROM Product WHERE restaurant_id = ?', (restaurant_id,))
    result = cursor.fetchall()
    con.close()
    return result

def find_user_addresses(customer_id):
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    query = 'SELECT id,phone_number,city,town,district,address,address_description FROM CustomerAddress WHERE customer_id = ?'
    cursor.execute(query, (customer_id,))
    result = cursor.fetchall()
    con.close()
    return result


def find_restaurant_address(product_id):
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    cursor.execute(
        'SELECT restaurant_id FROM Product WHERE id = ?', (product_id,))
    restaurant_id = cursor.fetchone()
    cursor.execute(
        'SELECT city, town FROM Restaurant WHERE id = ?', (restaurant_id[0],))
    result = cursor.fetchone()
    return result[0], result[1]
    # return City, Town


def find_new_orders(restaurant_id):
    con = sqlite3.connect('database.db')
    cursor = con.cursor()
    cursor.execute(
        'SELECT id, date, total_price, state, address_id FROM Order_ WHERE state <> ?', ('Teslim Edildi',))
    result = cursor.fetchall()
    con.close()
    return result


def find_delivered_orders(restaurant_id):
    con = sqlite3.connect('database.db')
    cursor = con.cursor()
    cursor.execute(
        'SELECT id, date, total_price, state, address_id FROM Order_ WHERE state = ?', ('Teslim Edildi',))
    result = cursor.fetchall()
    con.close()
    return result

def empty_basket():
    con = sqlite3.connect("basket.db")
    cursor = con.cursor()
    cursor.execute('DELETE FROM Basket')
    con.commit()
    con.close()

def get_order_details(order_id):
    con = sqlite3.connect('database.db')
    cursor = con.cursor()
    cursor.execute('SELECT product_id, product_amount FROM SoldProduct WHERE order_id = ?', (order_id,))
    result = cursor.fetchall()
    product_ids = []
    product_names = []
    product_amounts = []
    for i in result:
        product_ids.append(list(i)[0])
        product_amounts.append(list(i)[1])
    for product_id in product_ids:
        cursor.execute('SELECT name FROM Product WHERE id = ?', (product_id,))
        result = cursor.fetchone()
        product_names.append(list(result)[0])

    products_str = ""
    for product_amount, product_name in zip(product_amounts, product_names):
        products_str += str(product_amount) + "x " + product_name + "\n"

    cursor.execute('SELECT address_id, date, state FROM Order_ WHERE id = ?', (order_id,))
    result = list(cursor.fetchone())
    address_id = result[0]
    date = result[1]
    state = result[2]

    cursor.execute('SELECT customer_id, city, town, district, address, address_description, phone_number FROM CustomerAddress WHERE id = ?', (address_id,))
    result = list(cursor.fetchone())
    address = result[4] + " " + result[3] + " " + result[2] + "/" + result[1]
    customer_id = result[0]
    address_description = result[5]
    phone_number = result[-1]

    cursor.execute('SELECT name, surname FROM Customer WHERE id = ?', (customer_id,))
    result = list(cursor.fetchone())
    customer_name = result[0] + " " + result[1]

    con.close()
    return [customer_name ,products_str, date, address, address_description, state, phone_number]

def delete_address(address_id):
    con = sqlite3.connect('database.db')
    cursor = con.cursor()
    cursor.execute('DELETE FROM CustomerAddress WHERE id = ?', (address_id,))
    con.commit()
    con.close()